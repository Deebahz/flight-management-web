from django.http import JsonResponse
from .models import Pilot
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verify_rfid(request):

    if request.method == "POST":

        data = json.loads(request.body)

        uid = data.get("uid")

        try:

            pilot = Pilot.objects.get(
                rfid_uid=uid
            )

            return JsonResponse({
                "status":"success",
                "pilot_id":pilot.id,
                "pilot_name":pilot.name
            })

        except Pilot.DoesNotExist:

            return JsonResponse({
                "status":"error",
                "message":"Pilot not found"
            })

    return JsonResponse({
        "status":"invalid request"
    })

#def verify_rfid(request):

    if request.method == "POST":

        data = json.loads(
            request.body
        )

        uid = data.get("uid")

        try:

            pilot = Pilot.objects.get(
                rfid_uid=uid
            )

            return JsonResponse({
                "status":"success",
                "pilot_id":pilot.id,
                "pilot_name":pilot.name
            })

        except Pilot.DoesNotExist:

            return JsonResponse({
                "status":"error",
                "message":"Pilot not found"
            })

    return JsonResponse({
        "status":"invalid request"
    })