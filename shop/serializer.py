from django.db.models import fields 
from rest_framework import serializers
from .models import Product
from multiselectfield import MultiSelectField

SIZES = (
        ('XS', 'ExtraSmall'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
        ('XXL', '2ExtraLarge'),
    )
  

class ProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Product
        fields = ('name','description','price','size','subcategory')