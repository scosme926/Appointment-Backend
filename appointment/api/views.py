import json
from django.http import JsonResponse


def version_endpoint(request):
    return JsonResponse({
        "version": 2.0,
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
