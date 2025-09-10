from django.urls import path
from . import views

urlpatterns = [
    path('', views.PropertyListCreateView.as_view(), name='property-list-create'),
    path('<int:pk>/', views.PropertyDetailView.as_view(), name='property-detail'),
]