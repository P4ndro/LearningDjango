from django import forms
from .models import Post, Comment, Like


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post content here...',
                'rows': 10
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'post-slug-example'
            }),
            'banner': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
        help_texts = {
            'slug': 'URL-friendly version of the title (e.g., my-first-post)',
            'banner': 'Optional: Upload a banner image for your post'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control comment-textarea',
                'placeholder': 'Write your comment here...',
                'rows': 3,
                'maxlength': 500
            }),
        }
        labels = {
            'body': ''
        }

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['is_liked']
        widgets = {
            'is_liked': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        help_texts = {
            'is_liked': 'Like the post'
        }
    
