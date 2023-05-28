from django.urls import path

from . import views

app_name = 'family'

urlpatterns = [
    path('', views.family_list, name='family_list'),
    path('create/', views.family_create, name='family_create'),
    path('create_user/', views.create_user, name='create_user'),
    path('users/<str:email>/', views.user_detail), # ajouter ce motif sous notre autre motif de groupes
    path('user_update/', views.user_update, name='user_update'),
    path('family_update/', views.family_update, name='family_update'),


    # path('<int:pk>/', views.family_detail, name='family_detail'),
    # path('<int:pk>/update/', views.family_update, name='family_update'),
    # path('<int:pk>/delete/', views.family_delete, name='family_delete'),
]
