from rest_framework import generics, status
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer
import uuid

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    
    def perform_create(self, serializer):
        booking = serializer.validated_data['booking']
        payment = serializer.save(
            amount=booking.total_price,
            transaction_id=str(uuid.uuid4())
        )
        # Simulate payment processing
        payment.status = 'completed'
        payment.save()
        
        # Update booking status
        booking.status = 'confirmed'
        booking.save()

class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        return Payment.objects.filter(booking__guest=self.request.user).select_related('booking')