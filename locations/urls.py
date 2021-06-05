from django.urls import path
from . import views

urlpatterns = [
    path('<int:location_id>/', views.view_location,
         name='view_location'),
]
