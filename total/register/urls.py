from django.urls import path
from .views import register, registration_success

urlpatterns = [
    path('register/', register, name='register'),
    path('registration-success/', registration_success, name='registration_success'),
]
