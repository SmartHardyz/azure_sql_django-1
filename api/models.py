from datetime import timezone
from django.db import models

# Create your models here.


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"
    
class Product(models.Model):
    # Model representing a product available in a store
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    def __str__(self):
        return self.user_name