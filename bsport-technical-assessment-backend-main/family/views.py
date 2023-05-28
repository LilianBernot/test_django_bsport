from django.shortcuts import render, redirect
from .models import Family
from user.models import User
from .forms import FamilyForm, UserCreationForm, ChildFormSet

# Create your views here.
def family_list(request):
    families = Family.objects.all()
    return render(request, 'family/family_list.html', {'families': families})


def family_create(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        formset = ChildFormSet(request.POST, prefix='children')
        if form.is_valid() and formset.is_valid():
            # family = form.save()
            # for child_form in formset:
            #     child = child_form.cleaned_data.get('child')
            #     if child:
            #         family.children.add(child)
            if formset.cleaned_data['children'] and not form.cleaned_data['is_in_relationship']:
                formset['children'] = []
            form.save()
            return redirect('family:family_list')
    else:
        form = FamilyForm()
        formset = ChildFormSet(prefix='children')
    return render(request, 'family/family_create.html', {'form': form, 'formset': formset})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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