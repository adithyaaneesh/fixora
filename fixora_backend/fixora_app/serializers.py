from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers):
    Model = Service
    fields = '__all__'