from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

class Flight(models.Model):
    user = models.ForeignKey('auth.User',related_name='flights',
                             on_delete=models.CASCADE)
    origin = models.CharField(max_length=255, blank=False)
    destination = models.CharField(max_length=255, blank=False)
    flight_date =  models.DateTimeField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user)

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)