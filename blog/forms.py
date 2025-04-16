from django.forms import ModelForm
from .models import Comment, Post
from django.forms.widgets import HiddenInput, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'placeholder': 'Add your comment here...', 'class': 'form-control'}),
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'text': TextInput(attrs={'placeholder': 'Content', 'class': 'form-control'}),
        }