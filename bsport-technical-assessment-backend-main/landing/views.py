from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm

# langing
def landing_page(request):
    return render(request, 'landing/landing.html')


def login_view(request):
    print("In the login view")
    if request.method == 'POST': # the form has been submitted
        form = LoginForm(request.POST) 
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('family:family_list')
        
        else:
            return render(request, 'landing/login.html', {'error_message': 'Invalid email or password'})
    
    return render(request, 'landing/login.html')


def signup_view(request):
    return render(request, 'landing/signup.html')