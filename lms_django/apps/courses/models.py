from django.db import models

# Create your models here.
class courses(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=255)
    course_duration = models.IntegerField()
    course_price = models.IntegerField()