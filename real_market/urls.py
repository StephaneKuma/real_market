"""real_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from property.api.views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'streets', StreetViewSet)
router.register(r'property_types', PropertyTypeViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'sale_status', SaleStatusViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'gallery', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
