from django.shortcuts import render
from pilots.models import Pilot
from flights.models import FlightLog

from django.shortcuts import render
from .models import Aircraft

def dashboard(request):

    context = {

        "total_aircraft":
            Aircraft.objects.count(),

        "grounded_aircraft":
            Aircraft.objects.filter(
                status="GROUNDED"
            ).count(),

        "total_pilots":
            Pilot.objects.count(),

        "total_flights":
            FlightLog.objects.count(),

        "aircrafts":
            Aircraft.objects.all()
    }

    return render(
        request,
        "dashboard.html",
        context
    )

def aircraft_list(request):

    aircrafts = Aircraft.objects.all()

    return render(
        request,
        "aircraft/aircraft_list.html",
        {
            "aircrafts": aircrafts
        }
    )
from django.http import JsonResponse

def ping(request):
    return JsonResponse({
        "status": "ok",
        "message": "UAMS Online"
    })