from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from property.forms import PropertyForm
from .models import Property, Reservation
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
    
    return JsonResponse(serializer.data)
    
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
        
    
# POST property reservation
@api_view(['POST'])
def book_property(request,pk):
    try:
        start_date = request.POST.get('start_date','')
        end_date = request.POST.get('end_date','')
        number_of_nights= request.POST.get('number_of_nights','')
        guests = request.POST.get('guests','')
        total_price = request.POST.get('total_price','')
        
        # get property based on his id
        property = Property.objects.get(pk=pk)
        
        # create reservation
        Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            number_of_nights = number_of_nights,
            guests = guests,
            total_price = total_price,
            created_by= request.user
        )
        
    except Exception as e:
        print(e)
        
        return JsonResponse({'success':False})