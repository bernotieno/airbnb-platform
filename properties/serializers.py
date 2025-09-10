from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'is_primary']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    host_name = serializers.CharField(source='host.get_full_name', read_only=True)
    
    class Meta:
        model = Property
        fields = ['id', 'host', 'host_name', 'title', 'description', 'property_type', 
                 'address', 'city', 'country', 'price_per_night', 'max_guests', 
                 'bedrooms', 'bathrooms', 'amenities', 'is_available', 'images', 'created_at']
        read_only_fields = ['id', 'host', 'created_at']

class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title', 'description', 'property_type', 'address', 'city', 
                 'country', 'price_per_night', 'max_guests', 'bedrooms', 
                 'bathrooms', 'amenities', 'is_available']