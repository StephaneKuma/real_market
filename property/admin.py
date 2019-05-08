from django import forms
from django.contrib import admin
from .models import *

from ckeditor.widgets import CKEditorWidget


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)


class DistrictAdmin(admin.ModelAdmin):
    pass


admin.site.register(District, DistrictAdmin)


class StreetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Street, StreetAdmin)


class SaleStatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(SaleStatus, SaleStatusAdmin)


class PropertyTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(PropertyType, PropertyTypeAdmin)


class PropertyAdminForm(forms.ModelForm):
    property_desc = forms.CharField(widget=CKEditorWidget())
    location = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Property
        fields = '__all__'


class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm


admin.site.register(Property, PropertyAdmin)

admin.site.register(Schedule)

admin.site.register(Gallery)
