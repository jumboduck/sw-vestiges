from django.urls import path
from . import views

urlpatterns = [
    path('<int:location_id>/', views.view_location,
         name='view_location'),
    path('map/', views.locations_map,
         name='locations_map'),
]
