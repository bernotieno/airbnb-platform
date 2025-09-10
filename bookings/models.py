from django.db import models
from django.contrib.auth import get_user_model
from properties.models import Property

User = get_user_model()

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
        indexes = [
            models.Index(fields=['guest', 'status']),
            models.Index(fields=['property', 'check_in', 'check_out']),
            models.Index(fields=['status']),
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(check_out__gt=models.F('check_in')), name='valid_dates'),
        ]