from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Author

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CutLinkForm(forms.Form):
    URL = forms.URLField(help_text='Enter you URL address here',label="URL")

