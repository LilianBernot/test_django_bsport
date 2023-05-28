from django.urls import path

from . import views

app_name = 'family'

urlpatterns = [
    path('', views.family_list, name='family_list'),
    path('create_user/', views.create_user, name='create_user'),
    path('users/<str:email>/', views.detail_user), # ajouter ce motif sous notre autre motif de groupes
    # path('<str:user>/', views.detail_family), # ajouter ce motif sous notre autre motif de groupes

    path('update_user/', views.update_user, name='user_update'),
    path('update_family/', views.update_family, name='family_update'),
]
