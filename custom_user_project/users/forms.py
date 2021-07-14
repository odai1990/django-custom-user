from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


from .models import CustomUser





class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser        
        fields=('email','username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser        
        fields=('email','username')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')