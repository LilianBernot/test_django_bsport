from django.shortcuts import render, redirect
from .models import Family
from .forms import FamilyForm
from .forms import UserCreationForm

# Create your views here.
def family_list(request):
    families = Family.objects.all()
    return render(request, 'family/family_list.html', {'families': families})

def family_create(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family:family_list')
    else:
        form = FamilyForm()
    return render(request, 'family/family_create.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family:family_list') # to change with the unique identifier url of the user
    else:
        form = UserCreationForm()
    return render(request, 'family/create_user.html', {'form': form})