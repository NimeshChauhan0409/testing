from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CHOICES = [
    ('stock', 'stock'),
    ('outstock', 'ouststock'),
]

class Product(models.Model):
    productname=models.CharField(max_length=50)
    image=models.ImageField()
    image1=models.ImageField()
    image2=models.ImageField()
    price=models.IntegerField()
    my_field = models.CharField(max_length=20, choices=CHOICES)
    description = models.CharField(max_length=20)


class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    users=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total=models.IntegerField()

