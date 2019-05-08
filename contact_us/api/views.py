from rest_framework import viewsets

from contact_us.api.serializers import ContactSerializer
from contact_us.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-last_name')
    serializer_class = ContactSerializer
