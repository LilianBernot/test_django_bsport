from django.urls import path

from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
