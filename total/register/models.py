from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tgnic = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.pk:  # Только если объект создается впервые
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
