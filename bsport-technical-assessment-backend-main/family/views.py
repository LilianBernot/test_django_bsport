from django.shortcuts import render
from .models import Family

# Create your views here.
def family_list(request):
    # families = Family.objects.all()
    # return render(request, 'family/family_list.html', {'families': families})
    return render(request, 'family/family_list.html', {'families': [0, 1, 2]})
