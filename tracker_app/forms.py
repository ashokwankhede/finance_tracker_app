from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Transaction

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2', 'avatar']
