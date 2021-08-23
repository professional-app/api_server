from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('list_relationships', views.list_relationships, name='list_relationships'),
]
