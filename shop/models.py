from django.db import models

from django.contrib.auth.models import User

class Driver(models.Model):
    STATUS = (
        ('A', 'Available'),
        ('U', 'Unavailable'),
        ('I', 'Idle'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    gps_position = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS)

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)

class Seller(models.Model):
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
        ('I', 'Idle'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=300)
    shop_category = models.CharField(max_length=300)
    products = models.CharField(max_length=600)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=1, choices=STATUS)

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loaded = models.DateTimeField()
    delivered = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.CharField(max_length=600)
