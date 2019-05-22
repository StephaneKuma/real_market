from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from alert.api.views import AlertViewSet
from contact_us.api.views import ContactViewSet
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
router.register(r'contact', ContactViewSet)
router.register(r'alert', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
