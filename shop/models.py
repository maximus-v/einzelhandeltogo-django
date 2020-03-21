from django.db import models

from django.contrib.auth.models import User

# HELPER

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=300)

class Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latidude = models.DecimalField(max_digits=9, decimal_places=6)

# MAIN ENTITIES

class Driver(models.Model):
    STATUS = (
        ('A', 'Available'),
        ('U', 'Unavailable'),
        ('I', 'Idle'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    gps_position = models.ForeignKey('Location', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.user.username

class Buyer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
        ('I', 'Idle'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=300)
    # TODO: extract category to own model
    shop_category = models.OneToOneField(Category, on_delete=models.CASCADE)
    # TODO: extract products (maybe rather offered_services) to own model
    products = models.CharField(max_length=600)
    phonenumber = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.company_name


class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loaded = models.DateTimeField()
    delivered = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    transaction_content = models.CharField(max_length=600)

    def __str__(self):
        return self.transaction_content
