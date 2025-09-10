from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'property']
    
    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user).select_related('property', 'guest')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        return BookingSerializer
    
    def perform_create(self, serializer):
        booking = serializer.save(guest=self.request.user)
        # Calculate total price
        days = (booking.check_out - booking.check_in).days
        booking.total_price = booking.property.price_per_night * days
        booking.save()

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user).select_related('property', 'guest')