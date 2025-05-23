from django.urls import path

from . import api

urlpatterns =[
    path('',api.getProperties,name="api_properties_list"),
    path('create/', api.create_property, name='api_create_property'),
    path('<uuid:pk>/', api.property_details, name='api_property_detail'),
    path('<uuid:pk>/book/',api.book_property,name="api_book_property")

]
