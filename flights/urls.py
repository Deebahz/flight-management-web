from django.urls import path
from .views import analytics, process_flight

urlpatterns = [
    path(
        "process-flight/",
        process_flight
    ),
     path(
        'analytics/',
        analytics,
        name='analytics'
    ),
]