from django import forms
# from django.forms import formset_factory
from .models import Family

from user.models import User
from django.contrib.auth.forms import UserCreationForm


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['user', 'father', 'mother', 'father_relationship_rank', 'mother_relationship_rank', 'is_in_relationship', 'relationship', 'children']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     is_in_relationship = cleaned_data.get('is_in_relationship')
    #     children = cleaned_data.get('children')

    #     if not is_in_relationship and children:
    #         raise forms.ValidationError("Can't have children if not in a relationship.")
    
    #     return cleaned_data

# class ChildForm(forms.Form):
#     child = forms.ModelChoiceField(queryset=User.objects.all())

# ChildFormSet = formset_factory(ChildForm, extra=3)  # Set the initial number of child forms to 1


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')