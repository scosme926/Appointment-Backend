import json
import jwt
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from appointment.settings import SECRET_KEY
from .models import Appointment
from datetime import datetime


def version_endpoint(request):
    return JsonResponse({
        "version": 3.0,
    })


def hello_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)



        name = data.get("name")



        return JsonResponse({
            "msg": "Konichiwa " + name + "!",
        })
    else:
        return JsonResponse({
            "msg": "method not allowed",
        }, status=405)


def login_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("email")
        password = data.get("password")



        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({
                "msg": "username or password is incorrect",
            }, status=401)



        login(request, user)



        encoded_jwt = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")



        return JsonResponse({
            "token": encoded_jwt,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        })

    else:
        return JsonResponse({
            "msg": "method not allowed",
        }, status=405)



def register_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("fname")
        last_name = data.get("lname")
        email = data.get("email")
        password = data.get("password")
        username = email


        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()



        return JsonResponse({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
    else:
        return JsonResponse({
        "msg": "method not allowed",
        }, status=405)



def list_create_appointment_api_endpoint(request):
    if request.method == "GET":
        results = [
            {
                "id": 1,
                "appointment_services": "",
                "appointment_dt": "",
            }
        ]
        return JsonResponse({"results": results})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"Fill the forms"}, status=400 )


        appointment_services = data.get("appointment_services")
        appointment_dt = data.get("appointment_dt")
        appointment_dt = datetime.strptime(appointment_dt, "%a, %d %b %Y %H:%M:%S %Z")


        appointment = Appointment.objects.create(
            services=appointment_services,
            date_time=appointment_dt,
        )


        return JsonResponse({"console": "Appointment created"})
    else:
        return JsonResponse({"message" : "something went wrong, try again"}, status=405)
