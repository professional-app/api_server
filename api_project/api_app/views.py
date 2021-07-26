from django.shortcuts import render

# Create your views here.
import requests

from django.http import HttpResponse, JsonResponse

def anything(something):
    return  JsonResponse(requests.get(f'https://professional.app/wp-json/wp/v2/{something}').content.decode("ascii"), safe=False)

def index(request):
    return anything('pages')

def wolf(request):
    return anything('entity')
