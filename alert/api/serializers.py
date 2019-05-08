from rest_framework import serializers

from alert.models import Alert


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
