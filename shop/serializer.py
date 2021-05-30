from django.contrib.auth import get_user_model
from django.db.models import fields 
from rest_framework import serializers
from .models import Product ,Like,SubCategory
#from multiselectfield import MultiSelectField

SIZES = (
        ('XS', 'ExtraSmall'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
        ('XXL', '2ExtraLarge'),
    )
  

class ProductSerializer(serializers.ModelSerializer):
    def get_like(self,obj):
      request = self.context.get("request")
      user = request.user
      if request.user.is_authenticated:  
        if Like.objects.filter(user=user,product_id=obj.id):
          return 1
        else:
          return 0
      else:
        return 0    
    likes_product = serializers.SerializerMethodField('get_like')            
    class Meta:
        model = Product
        fields = ('id','name','description','price','size','subcategory','likes_product','image')
class MyProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('id','name','description','price','size','subcategory','image')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('product_id',)

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
      model = SubCategory
      fields = ('id','name','category')
