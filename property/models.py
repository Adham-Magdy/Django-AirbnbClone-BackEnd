import uuid

from django.db import models
from user_account.models import User
from django.conf import settings

# building property db model

class Property(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    guests = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=255)
    
    #favorite
    image = models.ImageField(upload_to='uploads/properties')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # relations
    landlord = models.ForeignKey(User,related_name="properties",on_delete=models.CASCADE)

    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'
    
# building reservation db model

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, related_name='reservations', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_nights = models.IntegerField()
    guests = models.IntegerField()
    total_price = models.FloatField()
    created_by = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)