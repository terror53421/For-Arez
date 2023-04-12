from django.db import models
from django.utils import timezone
from django.conf import settings 

"""Weather parameters DB"""
class Weather_check(models.Model):
    city = models.CharField(max_length=255)
    temp = models.IntegerField(null=True)
    joined_date = models.DateTimeField(null=True)
