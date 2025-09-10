from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentCreateView.as_view(), name='payment-create'),
    path('list/', views.PaymentListView.as_view(), name='payment-list'),
]