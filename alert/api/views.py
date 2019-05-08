from rest_framework import viewsets

from alert.api.serializers import AlertSerializer
from alert.models import Alert


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('-property_type')
    serializer_class = AlertSerializer
