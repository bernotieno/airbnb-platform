from rest_framework import serializers
from .models import Booking
from properties.serializers import PropertySerializer

class BookingSerializer(serializers.ModelSerializer):
    property_title = serializers.CharField(source='property.title', read_only=True)
    guest_name = serializers.CharField(source='guest.get_full_name', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'guest', 'guest_name', 'property', 'property_title', 
                 'check_in', 'check_out', 'guests', 'total_price', 'status', 'created_at']
        read_only_fields = ['id', 'guest', 'total_price', 'created_at']

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property', 'check_in', 'check_out', 'guests']
    
    def validate(self, attrs):
        if attrs['check_in'] >= attrs['check_out']:
            raise serializers.ValidationError("Check-out must be after check-in")
        
        property_obj = attrs['property']
        if attrs['guests'] > property_obj.max_guests:
            raise serializers.ValidationError("Too many guests for this property")
        
        # Check availability
        overlapping = Booking.objects.filter(
            property=property_obj,
            status__in=['confirmed', 'pending'],
            check_in__lt=attrs['check_out'],
            check_out__gt=attrs['check_in']
        ).exists()
        
        if overlapping:
            raise serializers.ValidationError("Property not available for selected dates")
        
        return attrs