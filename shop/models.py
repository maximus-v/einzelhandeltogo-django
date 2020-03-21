from django.db import models

from django.contrib.auth.models import User


class Driver(models.Model):
    STATUS = (
        ('A', 'Available'),
        ('U', 'Unavailable'),
        ('I', 'Idle'),
    )
    # TODO: make Driver inherit from User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    gps_position = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.user.username


class Buyer(models.Model):
    # TODO: make Buyer inherit from User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    # TODO: extract address to own model
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
        ('I', 'Idle'),
    )
    # TODO: make Seller inherit from User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=300)
    # TODO: extract category to own model
    shop_category = models.CharField(max_length=300)
    # TODO: extract products (maybe rather offered_services) to own model
    products = models.CharField(max_length=600)
    phonenumber = models.CharField(max_length=20)
    # TODO: extract address to own model
    address = models.CharField(max_length=300)
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
    # TODO: rather rename to transaction_content
    product = models.CharField(max_length=600)

    def __str__(self):
        return self.product
