from django.db import models

class Aircraft(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "ACTIVE"),
        ("MAINTENANCE_DUE", "MAINTENANCE_DUE"),
        ("GROUNDED", "GROUNDED"),
        ("IN_MAINTENANCE", "IN_MAINTENANCE"),
    ]

    registration_no = models.CharField(
        max_length=20,
        unique=True
    )

    aircraft_name = models.CharField(
        max_length=100
    )

    manufacturer = models.CharField(
        max_length=100
    )

    total_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    next_service_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=200
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.registration_no