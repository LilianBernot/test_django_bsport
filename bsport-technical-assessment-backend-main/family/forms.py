from django import forms
from .models import Family

from user.models import User
from django.contrib.auth.forms import UserCreationForm


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['user', 'father', 'mother']

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')