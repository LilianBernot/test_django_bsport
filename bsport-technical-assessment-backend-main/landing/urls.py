from django.contrib import admin
from django.urls import path

from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path("admin/", admin.site.urls), # admin site where you can manage your Django project's data
]