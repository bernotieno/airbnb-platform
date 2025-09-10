from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from properties.models import Property
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        # Create sample users
        if not User.objects.filter(email='host@example.com').exists():
            host = User.objects.create_user(
                username='host1',
                email='host@example.com',
                password='testpass123',
                first_name='John',
                last_name='Host',
                is_host=True
            )
            self.stdout.write('Created host user')

        if not User.objects.filter(email='guest@example.com').exists():
            guest = User.objects.create_user(
                username='guest1',
                email='guest@example.com',
                password='testpass123',
                first_name='Jane',
                last_name='Guest'
            )
            self.stdout.write('Created guest user')

        # Create sample properties
        host = User.objects.get(email='host@example.com')
        if not Property.objects.filter(host=host).exists():
            Property.objects.create(
                host=host,
                title='Beautiful Apartment in Downtown',
                description='A lovely 2-bedroom apartment with city views',
                property_type='apartment',
                address='123 Main St',
                city='New York',
                country='USA',
                price_per_night=Decimal('150.00'),
                max_guests=4,
                bedrooms=2,
                bathrooms=1,
                amenities=['wifi', 'kitchen', 'parking']
            )
            self.stdout.write('Created sample property')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))