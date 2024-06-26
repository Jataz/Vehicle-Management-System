from datetime import datetime
from rest_framework import serializers
from ..models import FuelType, Location, Province, Status, Vehicle,UserProfile
from django.db import transaction
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.contrib.auth.models import User


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ['id', 'fuel_name']

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'province_name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location_name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'status_name']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name'] 
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    province_name = serializers.ReadOnlyField(source='province.province_name')
    location_name = serializers.ReadOnlyField(source='location.location_name')
    province_id = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all(), write_only=True, source='province')
    location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), write_only=True, source='location')
    
    class Meta:
        model = UserProfile
        fields = ['id','user','first_name','last_name','province_id', 'location_id','province_name', 'location_name']
        
    
class VehicleSerializer(serializers.ModelSerializer):
    province_name = serializers.ReadOnlyField(source='province.province_name')
    location_name = serializers.ReadOnlyField(source='location.location_name')
    status_name = serializers.ReadOnlyField(source='status.status_name')
    fuel_name = serializers.ReadOnlyField(source='fuelType.fuel_name')
    province_id = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all(), write_only=True, source='province')
    location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), write_only=True, source='location')
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), write_only=True, source='status')
    fuelType_id = serializers.PrimaryKeyRelatedField(queryset=FuelType.objects.all(), write_only=True, source='fuelType')

    class Meta:
        model = Vehicle
        fields = ['id', 'province_id', 'location_id', 'status_id', 'fuelType_id','number_plate', 'vehicle_type',\
            'province_name', 'location_name', 'status_name','classis_number','engine_number','fuel_name']
        
