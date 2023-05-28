from django.shortcuts import render, redirect

# langing
def landing_page(request):
    return render(request, 'landing/landing.html')

def login_view(request):
    return render(request, 'landing/login.html')

def signup_view(request):
    return render(request, 'landing/signup.html')