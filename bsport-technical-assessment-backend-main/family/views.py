from django.shortcuts import render, redirect
from .models import Family
from user.models import User
from .forms import UserCreationForm, UserUpdateForm, FamilyUpdateForm, NewUserCreationForm
# from .forms import ChildFormSet
from django.contrib.auth.hashers import check_password


# family related
def family_list(request):
    families = Family.objects.all()
    for fam in families:
        print(fam.user.email, fam.is_in_relationship)
    return render(request, 'family/family_list.html', {'families': Family.objects.all()})


# user related
def create_user(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['password1'])
            Family.objects.create_family(user, form.cleaned_data['father'], form.cleaned_data['mother'], form.cleaned_data['father_relationship_rank'], form.cleaned_data['mother_relationship_rank'], form.cleaned_data['is_in_relationship'], form.cleaned_data['relationship'], form.cleaned_data['child'])
            return redirect('family:family_list') # to change with the unique identifier url of the user
    else:
        form = NewUserCreationForm()
    return render(request, 'family/create_user.html', {'form': form})


def detail_user(request, email):
    try: 
        # we get the corresponding User instance
        instance =  User.objects.get(email = email)
        return render(request,
            'family/detail_user.html',
            {'user': instance}) 
    except:
        return render(request,
            'family/detail_user.html',
            {'user': None}) 


def detail_family(request, user):
    try: 
        # we get the corresponding User instance
        print(user)
        instance =  Family.objects.get(user = user)
        return render(request,
            'family/detail_family.html',
            {'email': instance}) 
    except:
        return render(request,
            'family/detail_family.html',
            {'email': user, 'families':Family.objects.all()}) 

# updates
def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            new_last_name = form.cleaned_data['new_last_name']
            new_first_name = form.cleaned_data['new_first_name']

            try:
                user = User.objects.get(email=email) # we just verify that the password matches the email
                if check_password(password, user.password): # Django hashes the passwords so we have to use one of its functions to compare them
                    user.last_name = new_last_name
                    user.first_name = new_first_name

                    user.save()
                    return render(request,
                        'family/user_detail.html',
                        {'user': None}) 
                else:
                    form.add_error(None, 'Invalid password')
            
            except User.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    
    else:
        form = UserUpdateForm()
    
    return render(request, 'family/update_user.html', {'form': form})


def update_family(request):
    if request.method == 'POST':
        form = FamilyUpdateForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            new_child = form.cleaned_data['new_child']

            try:
                user = User.objects.get(email=email) # we just verify that the password matches the email
                
                if check_password(password, user.password): # Django hashes the passwords so we have to use one of its functions to compare them
                    family = Family.objects.get(user=user)
                    family.child = new_child
                    family.save()
                    return render(request, 'family/detail_family.html', {'family': family})
                else:
                    form.add_error(None, 'Invalid password')
            
            except User.DoesNotExist:
                form.add_error(None, 'Invalid email')
    
    else:
        form = FamilyUpdateForm()
    
    return render(request, 'family/update_family.html', {'form': form})