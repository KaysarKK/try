from rest_framework import serializers
from django.db import models
from .models import Device, City, Info

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = '__all__'

