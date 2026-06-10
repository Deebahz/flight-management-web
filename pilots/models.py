from django.db import models

class Pilot(models.Model):

    name = models.CharField(
        max_length=100
    )

    license_number = models.CharField(
        max_length=50,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    rfid_uid = models.CharField(
        max_length=50,
        unique=True
    )

    total_flight_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name