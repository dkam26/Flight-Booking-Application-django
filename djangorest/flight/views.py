
# Create your views here.
from rest_framework import generics
from .serializers import FlightSerializer
from .models import Flight
from rest_framework import permissions
from .permissions import IsOwner

class CreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)