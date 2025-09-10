# Airbnb Clone Backend API

A comprehensive Django REST Framework backend for an Airbnb-like platform with JWT authentication, GraphQL support, and async task processing.

## Features

- **User Management**: Registration, JWT authentication, profile management
- **Property Management**: CRUD operations for property listings with image support
- **Booking System**: Create and manage bookings with availability validation
- **Payment Processing**: Handle payment transactions for bookings
- **Review System**: Users can leave reviews and ratings for properties
- **GraphQL API**: Alternative query interface
- **Database Optimizations**: Indexes and query optimizations
- **Async Tasks**: Celery integration for background processing
- **API Documentation**: Auto-generated Swagger/OpenAPI docs

## Tech Stack

- Django 4.2 + Django REST Framework
- PostgreSQL database
- JWT authentication (djangorestframework-simplejwt)
- GraphQL (graphene-django)
- Celery + Redis for async tasks
- Swagger/OpenAPI documentation (drf-spectacular)
- Docker & Docker Compose

## Quick Start

### Using Docker (Recommended)

1. Clone and navigate to the project:
```bash
git clone https://github.com/bernotieno/airbnb-platform.git
cd airbnb-platform
```

2. Start services:
```bash
docker-compose up --build
```

3. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

4. Create superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login (get JWT tokens)
- `POST /api/users/refresh/` - Refresh JWT token

### Users
- `GET /api/users/` - List users
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user

### Properties
- `GET /api/properties/` - List properties (with filtering)
- `POST /api/properties/` - Create property
- `GET /api/properties/{id}/` - Get property details
- `PUT /api/properties/{id}/` - Update property
- `DELETE /api/properties/{id}/` - Delete property

### Bookings
- `GET /api/bookings/` - List user's bookings
- `POST /api/bookings/` - Create booking
- `GET /api/bookings/{id}/` - Get booking details
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Cancel booking

### Payments
- `POST /api/payments/` - Process payment
- `GET /api/payments/list/` - List user's payments

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Create review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

## Documentation

- **Swagger UI**: http://localhost:8000/api/schema/swagger-ui/
- **GraphQL**: http://localhost:8000/graphql/
- **Admin Panel**: http://localhost:8000/admin/

## Database Schema

The application uses optimized database models with proper indexing:

- **Users**: Custom user model with host capabilities
- **Properties**: Property listings with images and amenities
- **Bookings**: Reservation system with date validation
- **Payments**: Transaction tracking
- **Reviews**: Rating and comment system

## Performance Features

- Database query optimization with select_related and prefetch_related
- Strategic database indexes on frequently queried fields
- Redis caching for improved performance
- Pagination for large datasets
- Async task processing with Celery

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Starting Celery Worker
```bash
celery -A airbnb_platform worker -l info
```

## Production Deployment

1. Set `DEBUG=False` in environment variables
2. Configure proper `SECRET_KEY`
3. Set up production database
4. Configure static file serving
5. Set up proper CORS settings
6. Configure Celery with production broker

## License

MIT License