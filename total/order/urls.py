from django.urls import path, include
from .views import create_order, order_success

urlpatterns = [
    path('', create_order, name='create_order'),
    path('order-success/', order_success, name='order_success'),
]