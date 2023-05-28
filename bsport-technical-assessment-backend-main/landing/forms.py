from django import forms
# from django.forms import formset_factory
from user.models import User


class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 