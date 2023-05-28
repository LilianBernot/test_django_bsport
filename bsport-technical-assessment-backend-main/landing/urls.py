from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='landing/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', views.signup_view, name='signup'),
    # path("admin/", admin.site.urls), # admin site where you can manage your Django project's data
]