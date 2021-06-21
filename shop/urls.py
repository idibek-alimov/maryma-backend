from django.urls import path,include
from rest_framework import urlpatterns

from rest_framework.routers import SimpleRouter

from . import views

app_name = 'shop'

router = SimpleRouter()
router.register('orders',views.OrdersView)
router.register('',views.ProductViewSet)

# router.register('subcategory',views.SubCategoryListView)
# router.register('myproducts',views.MyProductsView)
urlpatterns = [
    path('myproducts',views.MyProductView.as_view(),name='myproduct'),
    path('subcategory/',views.SubCategoryView.as_view(),name='subcategory'),
    path('toorder/',views.ToOrderView.as_view(),name='toorder'),
    path('likecreatelist/<int:id>/',views.LikeCreateList.as_view(),name='createlike'),
    #path('orders/',views.OrdersView.as_view(),name='orders'),
    path('<int:category>/<str:search>/',views.CategoryProductFilter.as_view(),name='category_product_filter'),
    path('',include(router.urls)),   
]