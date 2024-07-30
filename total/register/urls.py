from django.urls import path
from .views import register, registration_success, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('registration-success/', registration_success, name='registration_success'),
    path('login/', user_login, name='login'),
]
