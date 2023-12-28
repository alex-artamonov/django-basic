
from django.http import HttpResponse
from django.http import JsonResponse  


def index(request):
    return HttpResponse("<h2>Hello from Django!</h2>")