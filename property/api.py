from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from property.forms import PropertyForm
from .models import Property
from .serializers import PropertySerializer,PropertyDetailSerializer

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getProperties(request):
    properties = Property.objects.all()
    serializers = PropertySerializer(properties,many=True)
    
    return JsonResponse({
        'data':serializers.data
    })


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def property_details(request,pk):
    property = Property.objects.get(pk=pk)
    serializer = PropertyDetailSerializer(property,many=False)
    
    return JsonResponse({
        'data',serializer.data
    })
    
# POST Property Data
@api_view(['POST', 'FILES'])
def create_property(request):
    form = PropertyForm(request.POST,request.FILES)
    
    # check form validation
    if form.is_valid():
        property = form.save(commit=False)
        property.landlord = request.user
        property.save()
        
        return JsonResponse({'success':True})
    
    else:
        print("error:",form.errors,form.non_field_errors)
        return JsonResponse({"errors":form.errors.as_json()})
        
    
