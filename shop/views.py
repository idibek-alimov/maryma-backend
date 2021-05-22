from django.shortcuts import render

# Create your views here.
from .models import Product
from .serializer import ProductSerializer
from rest_framework import generics,permissions,viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

