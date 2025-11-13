from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)
    

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like: {self.user.username} on {self.post.title}"
    
    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
    class Meta:
        ordering = ['created_at']


