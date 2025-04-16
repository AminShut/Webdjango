from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        label='',
        max_length=500,
        widget=forms.TextInput(attrs={'placeholder': 'Type your message...', 'required': True})
    )
