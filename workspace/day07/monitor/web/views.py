from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
import serializers 
import models
from rest_framework.decorators import api_view
# Create your views here.



class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset =  models.Host.objects.all()
    serializer_class = serializers.HostSerializer 
    
def monitor_data(request):
    print request.POST 
    
    return HttpResponse('service sends status report success!!')