from django import forms
from .models import Post, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # Hide the author field in the form, we'll overwrite it later
            'author': forms.HiddenInput(),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)