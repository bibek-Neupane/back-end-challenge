from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Control
from django.urls import reverse


class ControlAPITestCase(TestCase):


    def setUp(self):
        self.control = Control.objects.create(
            name = 'Single qubit driven',
            type = 'Primitive',
            maximum_rabi_rate = 63.00921,
            polar_angle = 0.00023
        )
        self.control.save()


    def test_control_creation(self):
        self.assertEquals(self.control.name, 'Single qubit driven')

    

    

        

