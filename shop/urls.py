from django.urls import path,include
from rest_framework import urlpatterns

from rest_framework.routers import SimpleRouter

from . import views

app_name = 'shop'

router = SimpleRouter()

router.register('',views.ProductViewSet)
#router.register('searchby/<str:query>',views.SearchViewSet)

urlpatterns = [
    path('',include(router.urls)),
   # path('search/<str:query>/',views.product_search,name='product_search'),
    path('likecreatelist/<int:id>/',views. LikeCreateList.as_view(),name='createlike'),
    path('<int:category>/<str:search>/',views.CategoryProductFilter.as_view(),name='category_product_filter'),
    

]