from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        label='You',
        max_length=500,
        widget=forms.Textarea(attrs={'placeholder': 'َAsk me anything...'})
    )
