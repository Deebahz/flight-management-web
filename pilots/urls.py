from django.urls import path
from .views import verify_rfid

urlpatterns = [
    path(
        'verify-rfid/',
        verify_rfid,
        name='verify-rfid'
    ),
]