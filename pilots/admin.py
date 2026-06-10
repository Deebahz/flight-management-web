from django.contrib import admin
from .models import Pilot

@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'license_number',
        'rfid_uid',
        'total_flight_hours'
    )

    search_fields = (
        'name',
        'license_number',
        'rfid_uid'
    )