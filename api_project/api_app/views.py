from django.shortcuts import render

# Create your views here.
import requests

from django.http import HttpResponse, JsonResponse


def make_api_call(path):
    return  JsonResponse(requests.get(f'https://professional.app/wp-json/wp/v2/{path}').content.decode("ascii"), safe=False)

#def list_relationships(request):
#    return make_api_call(f'entity?include={entity_id}&_fields=relationships')

def pages(request):
    return make_api_call('pages')

def entity(request):
    return make_api_call('entity')
