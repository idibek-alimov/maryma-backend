from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank,TrigramSimilarity
from rest_framework.response import Response
# Create your views here.
from .models import Product,Like
from .serializer import LikeSerializer, ProductSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics,permissions, serializers,viewsets,status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class SearchViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def retrieve(self,query):
        search_vector = SearchVector('name','description')
        search_query = SearchQuery(query)
        products  = Product.objects.annotate(
        similarity=TrigramSimilarity('name',query),
        ).filter(similarity__gt=0.1).order_by('-similarity')
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
class CategoryProductFilter(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self,*args,**kwargs):
        search_vector = SearchVector('name','description')
        search_query = SearchQuery(self.kwargs['search'])
        

        if self.kwargs['search'] == 'und':
            return Product.objects.filter(subcategory__id=self.kwargs['category'])
        elif self.kwargs['category'] == 0 :
            return Product.objects.annotate(
            similarity = TrigramSimilarity('name',self.kwargs['search']),
            ).filter(similarity__gt=0.1).order_by('-similarity')
        
        else :
            return Product.objects.annotate(
            similarity = TrigramSimilarity('name',self.kwargs['search']),
            ).filter(similarity__gt=0.1,subcategory__id=self.kwargs['category']).order_by('-similarity')    


class LikeCreateList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    def create(self, request,id, *args, **kwargs):
      serializer = LikeSerializer(data=request.data)
     
      if Like.objects.filter(user=request.user,product_id=id):
           Like.objects.filter(user=request.user,product_id=id).delete()
      elif serializer.is_valid():
          serializer.save(user=request.user)
          return super(LikeCreateList, self).create(request, *args, **kwargs)
          #super(LikeCreateList, self).create(request, *args, **kwargs)
          #return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )






