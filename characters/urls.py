from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_character, name='add_character'),
    path('<int:character_id>/', views.character_detail, name='character_detail'),
    path('edit/<int:character_id>/', views.edit_character, name='edit_character'),
    path('move/<int:destination_id>/',
         views.move_active_character, name='move_active_character'),
    path('view/', views.user_character, name='user_character'),
    path('switch/<int:character_id>/',
         views.change_active_character, name='change_active_character'),
    path('change_location/', views.view_active_character_destinations,
         name='view_active_character_destinations'),
    path('create_message/', views.create_message,
         name='create_message'),
    path('dexterity_test/', views.dexterity_test,
         name='dexterity_test'),
]
