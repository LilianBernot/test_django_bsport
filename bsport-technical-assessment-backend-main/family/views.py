from django.shortcuts import render, redirect
from .models import Family
from .forms import FamilyForm

# Create your views here.
def family_list(request):
    # families = Family.objects.all()
    # return render(request, 'family/family_list.html', {'families': families})
    return render(request, 'family/family_list.html', {'families': [0, 1, 2]})

def family_create(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('family:family_list')
    else:
        form = FamilyForm()
    return render(request, 'family/family_create.html', {'form': form})