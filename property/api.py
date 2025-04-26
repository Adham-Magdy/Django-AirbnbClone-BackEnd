from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .models import Property
from .serializers import PropertySerializer

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getProperties(request):
    properties = Property.objects.all()
    serializers = PropertySerializer(properties,many=True)
    
    return JsonResponse({
        'data':serializers.data
    })