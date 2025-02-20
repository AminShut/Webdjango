from django.forms import ModelForm
from .models import Comment,Post
from django.forms.widgets import HiddenInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']