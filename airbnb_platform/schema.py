import graphene
from graphene_django import DjangoObjectType
from users.models import User
from properties.models import Property
from bookings.models import Booking
from reviews.models import Review

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_host']

class PropertyType(DjangoObjectType):
    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'property_type', 'city', 'country', 'price_per_night', 'max_guests']

class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = ['id', 'check_in', 'check_out', 'guests', 'total_price', 'status']

class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'created_at']

class Query(graphene.ObjectType):
    all_properties = graphene.List(PropertyType)
    property_by_id = graphene.Field(PropertyType, id=graphene.Int(required=True))
    
    def resolve_all_properties(self, info):
        return Property.objects.filter(is_available=True)
    
    def resolve_property_by_id(self, info, id):
        return Property.objects.get(pk=id)

schema = graphene.Schema(query=Query)