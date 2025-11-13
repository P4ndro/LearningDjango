from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by('created_at')
    comment_count = comments.count()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('posts:page', slug=slug)
    else:
        form = CommentForm()
    
    like_count = post.likes.filter(is_liked=True).count()
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = post.likes.filter(user=request.user, is_liked=True).exists()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'form': form,
        'like_count': like_count,
        'user_has_liked': user_has_liked
    }
    return render(request, 'posts/post_page.html', context)


@login_required(login_url='register:login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('posts:page', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required(login_url='register:login')
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts!')
        return redirect('posts:page', slug=slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('posts:page', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


@login_required(login_url='register:login')
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts!')
        return redirect('posts:page', slug=slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('posts:posts')
    return redirect('posts:page', slug=slug)


@login_required(login_url='register:login')
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    
    if like.is_liked:
        like.is_liked = False
    else:
        like.is_liked = True
    like.save()
    
    messages.success(request, 'Like updated!')
    return redirect('posts:page', slug=slug)


@login_required(login_url='register:login')
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_slug = comment.post.slug
    
    if comment.author != request.user and comment.post.author != request.user:
        messages.error(request, 'You can only delete your own comments!')
        return redirect('posts:page', slug=post_slug)
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    
    return redirect('posts:page', slug=post_slug)


@login_required(login_url='register:login')
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_slug = comment.post.slug
    
    if comment.author != request.user:
        messages.error(request, 'You can only edit your own comments!')
        return redirect('posts:page', slug=post_slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('posts:page', slug=post_slug)
    else:
        form = CommentForm(instance=comment)
    
    context = {
        'form': form,
        'comment': comment,
        'post': comment.post
    }
    return render(request, 'posts/edit_comment.html', context)
