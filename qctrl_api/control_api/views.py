from django.shortcuts import render
from rest_framework import generics
from .serializers import ControlSerializer
from .models import Control


class ControlCreateView(generics.ListCreateAPIView):
    queryset = Control.objects.all()
    serializer_class =  ControlSerializer

    
    def do_create(self, serializer):
        serializer.save()



