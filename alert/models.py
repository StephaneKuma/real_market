from django.db import models

from property.models import PropertyType, Country


class Alert(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    min_surface = models.IntegerField()
    max_surface = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    #city = models.CharField(choices=[Country.objects.get(name=country)])

    def __str__(self):
        return "%s - Ville : au %s" % (self.property_type, self.country)

    class Meta:
        verbose_name = "Alerte de rescherche"
        verbose_name_plural = "Alertes de rescherche"
