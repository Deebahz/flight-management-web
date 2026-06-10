from django.urls import path
from .views import service_aircraft

urlpatterns = [
    path(
        "service-aircraft/",
        service_aircraft
    )
]