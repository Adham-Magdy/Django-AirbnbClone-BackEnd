from django.urls import path

from . import api

urlpatterns =[
    path('',api.getProperties,name="api_properties_list")
]