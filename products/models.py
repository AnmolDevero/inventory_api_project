from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateTimeField(default=timezone.now) 
    in_stock = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name 
