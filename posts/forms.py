from django import forms
from .models import Post


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

