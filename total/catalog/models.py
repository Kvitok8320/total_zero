from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catalog/img/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

