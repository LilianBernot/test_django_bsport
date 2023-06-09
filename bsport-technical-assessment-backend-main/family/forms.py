from django import forms
# from django.forms import formset_factory

from user.models import User
from django.contrib.auth.forms import UserCreationForm

# trying to implement the multiple children aspect
# class ChildForm(forms.Form):
#     child = forms.ModelChoiceField(queryset=User.objects.all())

# ChildFormSet = formset_factory(ChildForm, extra=3)  # Set the initial number of child forms to 1


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

class NewUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    father = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    father_relationship_rank = forms.IntegerField(min_value=1, max_value=5, required=False)
    mother = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    mother_relationship_rank = forms.IntegerField(min_value=1, max_value=5, required=False)
    
    is_in_relationship = forms.BooleanField(required=False)
    relationship = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    child = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    def clean(self):
        cleaned_data = super().clean()

        # verifying the passwords are the same
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        # verifying the father and mother are given
        father = cleaned_data.get('father')
        mother = cleaned_data.get('mother') 
        if not father or not mother:
            raise forms.ValidationError("The user needs a father and a mother.")

        # verifying the child corresponds to somebody in relationship
        is_in_relationship = cleaned_data.get('is_in_relationship')
        children = cleaned_data.get('child')
        if not is_in_relationship and children:
            raise forms.ValidationError("Can't have children if not in a relationship.")

        return cleaned_data


class UserUpdateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) # makes the password blank appear differently 
    
    new_last_name = forms.CharField(max_length=255, required=False)
    new_first_name = forms.CharField(max_length=255, required=False)


class FamilyUpdateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) # makes the password blank appear differently 
    
    new_status = forms.BooleanField(required=False)
    new_relationship = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    new_child = forms.ModelChoiceField(queryset=User.objects.all(), required=False)