from django.db import models

# Create your models here.

class Flight(models.Model):
    user = models.CharField(max_length=255, blank=False)
    origin = models.CharField(max_length=255, blank=False)
    destination = models.CharField(max_length=255, blank=False)
    flight_date =  models.DateTimeField()

