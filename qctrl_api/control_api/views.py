from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import ControlSerializer
from .models import Control
from django.db.models import Q
import csv, io
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#Create, Search and List view w/ mixins to combine the functionalities
class ControlCreateView(mixins.CreateModelMixin, generics.ListAPIView): 
    #queryset = Control.objects.all()
    serializer_class =  ControlSerializer

    def get_queryset(self):
        qs=Control.objects.all()
        #Basic Search 
        query = self.request.GET.get("q")
        if query is not None: 
            qs = qs.filter(
                Q(name__icontains = query) |
                Q(type__icontains = query)).distinct()
        return qs


    def create(self, serializer):
        serializer.save()


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
#DetailView - Retrieve Update and Delete 
class ControlRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView): 
    lookup_field = 'pk'
    queryset = Control.objects.all()
    serializer_class =  ControlSerializer

      
class CsvUploadView(APIView):
    def get(self, request):
        queryset = Control.objects.all()
        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar = "|") :
                 control = Control.objects.update_or_create(
                      name=column[0],
                      type=column[1],
                      maximum_rabi_rate=column[2],
                      polar_angle=column[3],
                 )
                 control.save()



    
    
       
                

            

