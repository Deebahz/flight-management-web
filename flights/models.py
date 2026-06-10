from django.db import models
from pilots.models import Pilot
from aircraft.models import Aircraft

class FlightLog(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "ACTIVE"),
        ("COMPLETED", "COMPLETED")
    ]

    pilot = models.ForeignKey(
        Pilot,
        on_delete=models.CASCADE
    )

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE
    )

    check_in = models.DateTimeField()

    check_out = models.DateTimeField(
        null=True,
        blank=True
    )

    flight_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return f"{self.pilot.name} - {self.aircraft.registration_no}"