"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view 
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Maryam API'
API_DESCRIPTION = 'A Web API for creating and editing products.'
schema_view = get_swagger_view(title =API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', schema_view),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    path('swagger-docs/',schema_view),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/', # new
          include('rest_auth.registration.urls')),
    path('',include('shop.urls',namespace='shop')),
]
