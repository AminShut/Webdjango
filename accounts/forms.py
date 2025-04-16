from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'age')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the password help text
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    def clean_password1(self):
        """
        Override password validation to show specific error messages only when rules are violated
        """
        password = self.cleaned_data.get('password1')
        
        # Empty error list to add specific messages as needed
        error_messages = []
        
        # Check each password rule and add specific error only if violated
        if len(password) < 8:
            error_messages.append('Password must be at least 8 characters long.')
            
        if not any(char.isdigit() for char in password):
            error_messages.append('Password must contain at least one number.')
            
        if not any(char.isalpha() for char in password):
            error_messages.append('Password must contain at least one letter.')
            
        if password.isalnum():
            error_messages.append('Password must contain at least one special character (like @, #, $).')
            
        if password.lower() == password:
            error_messages.append('Password must contain both uppercase and lowercase letters.')
            
        # If any error found, raise validation error
        if error_messages:
            raise forms.ValidationError(error_messages)
            
        return password

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')