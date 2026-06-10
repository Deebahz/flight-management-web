from django.http import JsonResponse
from django.utils import timezone
from decimal import Decimal

from django.db.models import Sum
from django.shortcuts import render

from pilots.models import Pilot
from aircraft.models import Aircraft
from .models import FlightLog

from aircraft.utils import update_aircraft_status

import json

def analytics(request):

    aircraft_hours = (
        FlightLog.objects
        .values(
            'aircraft__registration_no'
        )
        .annotate(
            total=Sum('flight_hours')
        )
    )

    return render(
        request,
        "analytics.html",
        {
            "aircraft_hours": aircraft_hours
        }
    )

def process_flight(request):

    if request.method != "POST":

        return JsonResponse({
            "status":"error"
        })

    data = json.loads(request.body)

    uid = data.get("uid")
    aircraft_id = data.get("aircraft_id")

    try:

        pilot = Pilot.objects.get(
            rfid_uid=uid
        )

    except Pilot.DoesNotExist:

        return JsonResponse({
            "status":"error",
            "message":"Pilot not found"
        })

    aircraft = Aircraft.objects.get(
        id=aircraft_id
    )

    if aircraft.status == "GROUNDED":

        return JsonResponse({
            "status":"error",
            "message":"Aircraft grounded"
        })

    active_flight = FlightLog.objects.filter(
        pilot=pilot,
        status="ACTIVE"
    ).first()

    if active_flight:

        active_flight.check_out = timezone.now()

        duration = (
            active_flight.check_out
            - active_flight.check_in
        )

        hours = round(
            duration.total_seconds()/3600,
            2
        )

        active_flight.flight_hours = hours
        active_flight.status = "COMPLETED"
        active_flight.save()

        pilot.total_flight_hours += Decimal(
            str(hours)
        )

        pilot.save()

        aircraft.total_hours += Decimal(
            str(hours)
        )

        aircraft.save()

        update_aircraft_status(
            aircraft
        )

        return JsonResponse({
            "status":"success",
            "action":"CHECK_OUT",
            "hours":hours
        })

    FlightLog.objects.create(
        pilot=pilot,
        aircraft=aircraft,
        check_in=timezone.now()
    )

    return JsonResponse({
        "status":"success",
        "action":"CHECK_IN"
    })

