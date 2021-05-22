from django.urls import path,include
from rest_framework import urlpatterns

from rest_framework.routers import SimpleRouter
from .views import ProductViewSet

app_name = 'shop'

router = SimpleRouter()

router.register('',ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
]