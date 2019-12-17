from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from control_api.models import Control
from django.urls import reverse
from rest_framework.test import APIClient



class ModelTestCase(TestCase):
    

    def setUp(self):
        control = Control.objects.create(
            name = 'Single qubit driven',
            type = 'Primitive',
            maximum_rabi_rate = 63.00921,
            polar_angle = 0.00023
        )
        control.save()


    def test_control_creation(self):
        control_count = Control.objects.count()
        self.assertEquals(control_count,1)
    

class ViewAPITestCase(TestCase):


    def setUp(self):
        control = Control.objects.create(
            name = 'Single qubit driven',
            type = 'Primitive',
            maximum_rabi_rate = 63.00921,
            polar_angle = 0.00023
        )
        control.save()


    def test_api_can_create_a_control(self):
        control ={'name' :'Single qubit driven', 'type': 'Primitive', 'maximum_rabi_rate': '64.0002', 'polar_angle': '0.0021'}
        response = self.client.post(
            reverse("control_create"), 
            control,
            format = "json"
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_control(self):
        response = self.client.get(
            reverse('control_create'),
            format="json"
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_api_can_delete_control(self):
        control = Control.objects.get()
        response = self.client.delete(
            reverse('control_rud',
            kwargs={'pk': control.pk}),
            format="json",
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_can_update_control(self):
        control = Control.objects.get()
        control_change_data = {'name': 'Two-Qubit Parametric Drive', 
                               'type': 'Primitive', 
                               'maximum_rabi_rate': '64.0002',
                               'polar_angle': '0.0021'}
        response = self.client.post(
            reverse('control_rud', 
            kwargs={'pk': control.pk}),
            control_change_data, 
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        #print(response.data)
   
    


        

