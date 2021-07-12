from django.shortcuts import render

# Create your views here.
import requests

from django.http import HttpResponse, JsonResponse


def index(request):
    return JsonResponse(requests.get('https://professional.app/wp-json/wp/v2/entity?slug=goat&_fields=id').content.decode("ascii"), safe=False)
