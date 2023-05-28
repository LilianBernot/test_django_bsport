from django.shortcuts import render, redirect
from .models import Family
from user.models import User
from .forms import FamilyForm, UserCreationForm, UserUpdateForm, FamilyUpdateForm
# from .forms import ChildFormSet
from django.contrib.auth.hashers import check_password


# family related
def family_list(request):
    families = Family.objects.all()
    return render(request, 'family/family_list.html', {'families': families})


def family_create(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family:family_list')

    # try to implement the multiple children aspect
        # formset = ChildFormSet(request.POST, prefix='children')
        # if form.is_valid() and formset.is_valid():
            # family = form.save()
            # for child_form in formset:
            #     child = child_form.cleaned_data.get('child')
            #     if child:
            #         family.children.add(child)
            # if formset.cleaned_data['children'] and not form.cleaned_data['is_in_relationship']:
            #     formset['children'] = []
            # form.save()
            # return redirect('family:family_list')
    else:
        form = FamilyForm()
        # formset = ChildFormSet(prefix='children')
    # return render(request, 'family/family_create.html', {'form': form, 'formset': formset})
    return render(request, 'family/family_create.html', {'form': form})


# user related
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['password1'])
            return redirect('family:family_list') # to change with the unique identifier url of the user
    else:
        form = UserCreationForm()
    return render(request, 'family/create_user.html', {'form': form})


def user_detail(request, email):
    try: 
        # we get the corresponding User instance
        instance =  User.objects.get(email = email)
        return render(request,
            'family/user_detail.html',
            {'user': instance}) 
    except:
        return render(request,
            'family/user_detail.html',
            {'user': None}) 



# updates
def user_update(request):
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
    
    return render(request, 'family/user_update.html', {'form': form})


def family_update(request):
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
                    return render(request,
                        'family/family_list.html',
                        {'user': None}) 
                else:
                    form.add_error(None, 'Invalid password')
            
            except User.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    
    else:
        form = FamilyUpdateForm()
    
    return render(request, 'family/family_update.html', {'form': form})