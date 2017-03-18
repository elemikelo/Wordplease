from django import forms

from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text_introduction', 'body_post', 'url', 'category', 'published_date', 'privacy']
        widgets = {
            'published_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
