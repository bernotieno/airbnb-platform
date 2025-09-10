from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'host', 'property_type', 'city', 'price_per_night', 'is_available']
    list_filter = ['property_type', 'city', 'country', 'is_available']
    search_fields = ['title', 'city', 'host__username']
    inlines = [PropertyImageInline]