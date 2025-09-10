from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    guest_name = serializers.CharField(source='guest.get_full_name', read_only=True)
    property_title = serializers.CharField(source='property.title', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'guest', 'guest_name', 'property', 'property_title', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'guest', 'created_at']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['property', 'rating', 'comment']