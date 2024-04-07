from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
      
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()

   def __str__(self):
     return self.name

class Delivery(models.Model):
  delivery_date = models.DateField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()

class Purchase(models.Model):
  supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
  purchase_date = models.DateField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Sale(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  sale_date = models.DateField()