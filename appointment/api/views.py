import json
import jwt
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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
        username = data.get("username")
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
        })

    else:
        return JsonResponse({
            "msg": "method not allowed",
        }, status=405)



def register_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")
        password = data.get("password")



        user = User.objects.create_user(email, password)
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
