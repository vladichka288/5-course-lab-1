from django.db import models
from django.conf import settings
from django.contrib import admin


class PhoneNumber(models.Model):
    book_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    phone_number1 = models.CharField(max_length=50)
    phone_number2 = models.CharField(max_length=50)


admin.site.register(PhoneNumber)
