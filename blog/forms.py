from django.forms import ModelForm
from .models import Comment
from django.forms.widgets import HiddenInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text','author','post']

        widgets = {
            'author': HiddenInput(),
            'post': HiddenInput()
        }