from django.test import TestCase
import datetime
# Create your tests here.
from .models import Flight
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = 'kamara'
        self.origin =  'Kampala'
        self.destination = 'Boston'
        self.flight_date = datetime.datetime.now()
        self.flight_data = {'user':self.user, 'origin': self.origin, 'destination': self.destination, 'flight_date': self.flight_date}
        self.response = self.client.post(
            reverse('create'),
            self.flight_data,
            format="json")



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
        change_flight = {'user':self.user, 'origin': 'NewYork', 'destination': self.destination, 'flight_date': self.flight_date}
        res = self.client.put(
            reverse('details', kwargs={'pk': flight.id}),
            change_flight, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_flight(self):
        flight = Flight.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': flight.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

