from rest_framework import serializers
from .models import Control

class ControlSerializer(serializers.ModelSerializer):


    class Meta:
        model = Control
        fields = ('id', 'name', 'type', 'maximum_rabi_rate', 'polar_angle')
        