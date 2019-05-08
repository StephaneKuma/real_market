from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=400)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s au sujet de %s" % (self.first_name, self.last_name, self.subject)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
