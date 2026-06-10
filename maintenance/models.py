from django.db import models
from aircraft.models import Aircraft

class MaintenanceRecord(models.Model):

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE
    )

    service_date = models.DateTimeField(
        auto_now_add=True
    )

    engineer_name = models.CharField(
        max_length=100
    )

    remarks = models.TextField()

    hours_at_service = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    next_service_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.aircraft.registration_no}"