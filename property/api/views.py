# from property.models import Country, City
from rest_framework import viewsets
from .serializers import *


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('-name')
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('-name')
    serializer_class = CitySerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by('-name')
    serializer_class = DistrictSerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all().order_by('-name')
    serializer_class = StreetSerializer


class SaleStatusViewSet(viewsets.ModelViewSet):
    queryset = SaleStatus.objects.all().order_by('-name')
    serializer_class = SaleStatusSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('-name')
    serializer_class = ScheduleSerializer


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all().order_by('-name')
    serializer_class = PropertyTypeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('-name')
    serializer_class = PropertySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-id')
    serializer_class = GallerySerializer
