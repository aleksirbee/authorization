from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input", "type": "text", "size": "40",
        "placeholder": "Enter username",
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input", "type": "email", "size": "40",
        "placeholder": "Enter email",
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input", "type": "password", "size": "40",
        "placeholder": "Enter Password",
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input", "type": "password", "size": "40",
        "placeholder": "Confirm password",
    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username',
        'style': 'width: 300px;',  # Изменение размера
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password',
        'style': 'width: 300px;',  # Изменение размера
    }))