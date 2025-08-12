from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    c_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    re_password = models.CharField(max_length=255)
    is_django = models.BooleanField()
