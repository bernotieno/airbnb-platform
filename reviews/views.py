from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, ReviewCreateSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.select_related('guest', 'property')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property', 'rating']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewCreateSerializer
        return ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(guest=self.request.user).select_related('guest', 'property')