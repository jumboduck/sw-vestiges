from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_character, name='add_character'),
    path('<int:character_id>/', views.character_detail, name='character_detail'),
    path('edit/<int:character_id>/', views.edit_character, name='edit_character'),
    path('move/<int:destination_id>/',
         views.move_active_character, name='move_active_character')
]
