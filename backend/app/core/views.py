from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Olá do Django Backend!"})