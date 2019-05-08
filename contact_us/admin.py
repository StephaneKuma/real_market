from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from contact_us.models import Contact


class ContactAdminForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorWidget())


class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm


admin.site.register(Contact, ContactAdmin)
