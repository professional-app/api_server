from django.shortcuts import render

# Create your views here.
import requests

from professionals import Entity
import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

def get_remote_api(query):
    return requests.get(f'https://professional.app/wp-json/wp/v2/{query}').content.decode("ascii")

def get_remote_entity(entity_id=0):
    entity = Entity()
    if not entity_id:
        entity.Invalidate()
        return entity

    try:
        entity_json = json.loads(get_remote_api(f"entity?include={entity_id}"))[0]

        entity.uniqueId = entity_json["id"]
        entity.name = entity_json["title"]["rendered"]
        for i in entity_json["interests"]:
            entity.interests.append(i["post_title"])
        for a in entity_json["activities"]:
            entity.activities.append(a["post_title"])

        entity.MakeValid()
        return entity

    except Exception as e:
        entity.Invalidate()
        return entity

def index(request):
    entity = get_remote_entity(request.GET["entity"])
    if entity.IsValid():
        return JsonResponse(entity.ToJSON(), safe=False)
    else:
        return HttpResponseBadRequest("Invalid entity request.")

def wolf(request):
    return anything('entity')
