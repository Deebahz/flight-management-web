from django.urls import path
from .views import aircraft_list, dashboard

urlpatterns = [
    path(
        "",
        aircraft_list,
        name="aircraft-list"
    ),
      
    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),
]