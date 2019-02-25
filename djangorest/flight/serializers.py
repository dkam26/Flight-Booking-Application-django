from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Flight
        fields = ('id' , 'user', 'origin', 'destination', 'flight_date')