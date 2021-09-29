from django.shortcuts import render

# Create your views here.
import requests
import logging

from professionals import Entity
import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

def get_remote_api(query):
    query_string = f'https://professional.app/wp-json/wp/v2/{query}'
    logging.info(f"Running query: {query_string}")
    return requests.get(query_string).content.decode("ascii")

def get_remote_entity(entity_id=0):
    entity = Entity()
    if not entity_id:
        entity.Invalidate()
        return entity

    try:
        entity_json = json.loads(get_remote_api(f"entity?include={entity_id}"))[0]

        entity.uniqueId = entity_json["id"]
        entity.name = entity_json["title"]["rendered"]
        entity.image_url = json.loads(get_remote_api(f"media?include={entity_json['featured_media']}"))[0]["guid"]["rendered"]
        for i in entity_json["interests"]:
            entity.interests.append(i["post_title"])
        for a in entity_json["activities"]:
            entity.activities.append(a["post_title"])

        entity.MakeValid()
        return entity

    except Exception as e:
        entity.Invalidate()
        return entity

def v1(request):
    if "entity" not in request.GET:
        return HttpResponseBadRequest("Please specify an entity with ?entity=0000")

    entity = get_remote_entity(request.GET["entity"])
    logging.info(f"Got entity: {entity}")
    if entity.IsValid():
        return JsonResponse(entity.ToJSON(), safe=False)
    else:
        return HttpResponseBadRequest("Invalid entity request.")

def index(request):
    return HttpResponse("It works!")