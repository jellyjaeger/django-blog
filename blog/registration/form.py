from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegisteredform(UserCreationForm):
    email = forms.EmailField(max_length=40)
    class meta:
        model = User
        fields = ['username','email','password1','password2']

