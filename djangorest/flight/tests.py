from django.test import TestCase
import datetime
# Create your tests here.
from .models import Flight
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="kamara")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.origin =  'Kampala'
        self.destination = 'Boston'
        self.flight_date = datetime.datetime.now()
        self.flight_data = {'user':self.user.id, 'origin': self.origin, 'destination': self.destination, 'flight_date': self.flight_date}
        self.response = self.client.post(
            reverse('create'),
            self.flight_data,
            format="json")

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/flights/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_model_can_create_a_flight(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_flight(self):
         flight = Flight.objects.get()
         response = self.client.get(
            reverse('details',
            kwargs={'pk': flight.id}), format="json")
         self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_flight(self):
        flight = Flight.objects.get()
        change_flight = {'user':'kamara', 'origin': 'NewYork', 'destination': 'Boston', 'flight_date': datetime.datetime.now()}
        res = self.client.put(
            reverse('details', kwargs={'pk': flight.id}),
            change_flight, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_flight(self):
        flight = Flight.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': flight.id}),
            format="json",
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

