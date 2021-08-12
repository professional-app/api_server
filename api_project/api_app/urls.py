from django.urls import path

from . import views

urlpatterns = [
    path('pages', views.pages, name='pages'),
    path('entity', views.entity, name='entity'),
    #path('list_relationships', views.list_relationships, name='list_relationships'),
]
