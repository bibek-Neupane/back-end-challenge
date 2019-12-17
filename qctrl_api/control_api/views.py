from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import ControlSerializer
from .models import Control
from django.db.models import Q


class ControlCreateView(mixins.CreateModelMixin, generics.ListAPIView): #Create, Search and List view w/ mixins to combine the functionalities
    queryset = Control.objects.all()
    serializer_class =  ControlSerializer

    def get_queryset(self):
        qs=Control.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains = query) |
                Q(type__icontains = query)).distinct()
        return qs

    def do_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class ControlRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    lookup_field = 'pk'
    queryset = Control.objects.all()
    serializer_class =  ControlSerializer

