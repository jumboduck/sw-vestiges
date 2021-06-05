from django.urls import path
from . import views

urlpatterns = [
    path('add_character/', views.add_character, name='add_character')
]
