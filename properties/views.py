from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Property
from .serializers import PropertySerializer, PropertyCreateSerializer

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.select_related('host').prefetch_related('images')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['property_type', 'city', 'country', 'is_available']
    search_fields = ['title', 'description', 'city', 'country']
    ordering_fields = ['price_per_night', 'created_at']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PropertyCreateSerializer
        return PropertySerializer
    
    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.select_related('host').prefetch_related('images')
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PropertyCreateSerializer
        return PropertySerializer