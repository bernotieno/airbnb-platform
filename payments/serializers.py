from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    booking_id = serializers.IntegerField(source='booking.id', read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'booking_id', 'amount', 'status', 'payment_method', 'transaction_id', 'created_at']
        read_only_fields = ['id', 'transaction_id', 'created_at']

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['booking', 'payment_method']