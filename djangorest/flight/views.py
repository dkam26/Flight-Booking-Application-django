
# Create your views here.
from rest_framework import generics
from .serializers import FlightSerializer
from .models import Flight

class CreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer