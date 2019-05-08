from rest_framework import serializers

from property.models import (
    Country,
    City,
    District,
    Street,
    SaleStatus,
    Schedule,
    PropertyType,
    Property,
    Gallery
)


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'


class SaleStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaleStatus
        fields = '__all__'


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='gallery-detail'
    )

    class Meta:
        model = Property
        fields = ('url', 'id', 'name', 'street', 'postcode', 'property_type',
                  'sale_status', 'furnished', 'price', 'rooms', 'bathrooms', 'parking',
                  'property_desc', 'location', 'schedule', 'floor', 'featured', 'images')


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
