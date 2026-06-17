from django.http import JsonResponse
from aircraft.models import Aircraft
from .models import MaintenanceRecord

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def service_aircraft(request):

    if request.method != "POST":

        return JsonResponse({
            "status":"error"
        })

    data = json.loads(
        request.body
    )

    aircraft_id = data.get(
        "aircraft_id"
    )

    engineer = data.get(
        "engineer"
    )

    remarks = data.get(
        "remarks"
    )

    aircraft = Aircraft.objects.get(
        id=aircraft_id
    )

    next_service = (
        aircraft.total_hours
        + 200
    )

    MaintenanceRecord.objects.create(
        aircraft=aircraft,
        engineer_name=engineer,
        remarks=remarks,
        hours_at_service=aircraft.total_hours,
        next_service_hours=next_service
    )

    aircraft.next_service_hours = (
        next_service
    )

    aircraft.status = "ACTIVE"

    aircraft.save()

    return JsonResponse({
        "status":"success"
    })