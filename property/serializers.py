from rest_framework import serializers

from .models import Property
from user_account.serializers import UserDetailSerializer


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url'


        )


class PropertyDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only = True,many=False)
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'description',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord'
        )
