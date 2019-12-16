from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Control
from django.urls import reverse


class ModelTestCase(TestCase):


    def setUp(self):
        self.control = Control.objects.create(
            name = 'Single qubit driven',
            type = 'Primitive',
            maximum_rabi_rate = 63.00921,
            polar_angle = 0.00023
        )


    def test_control_creation(self):
        self.assertEquals(self.control.name, 'Single qubit driven')

    
class ViewTestCase(TestCase):


    def setUp(self):
        self.client = APIClient()
        self.control_data = {'name':'Single qubit driven'}
        self.response = self.client.post(
            reverse('create'),
            self.control_data,
            format = "json"
        )


    def test_api_can_create_a_control(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    

        

