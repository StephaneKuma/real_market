from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'


class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.country)

    class Meta:
        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'


class District(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quartier'
        verbose_name_plural = 'Quartiers'


class Street(models.Model):
    name = models.CharField(max_length=150)
    district = models.ForeignKey(District, related_name='streets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rue'
        verbose_name_plural = 'Rues'


class PropertyType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type de Propriété'
        verbose_name_plural = 'Types de Propriété'


class SaleStatus(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type de marché'
        verbose_name_plural = 'Types de marché'


class Schedule(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'


class Property(models.Model):
    name = models.CharField(max_length=150)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=150, blank=True)
    image = models.ImageField(default=None, blank=True, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    sale_status = models.ForeignKey(SaleStatus, on_delete=models.CASCADE)
    furnished = models.NullBooleanField()
    price = models.FloatField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.BooleanField()
    property_desc = models.TextField()
    location = models.TextField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    floor = models.BooleanField()
    featured = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Propriété'
        verbose_name_plural = 'Propriétés'


class Gallery(models.Model):
    picture = models.ImageField(default=None, blank=True, null=True, upload_to='property/uploads/gallery')
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return '%s ' % self.picture

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
