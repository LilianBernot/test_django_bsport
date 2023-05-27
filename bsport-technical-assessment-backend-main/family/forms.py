from django import forms
from .models import Family

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['user', 'father', 'mother']