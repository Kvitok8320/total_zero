from django.urls import path, include
from .views import create_order

urlpatterns = [
    path('', create_order, name='create_order'),

]