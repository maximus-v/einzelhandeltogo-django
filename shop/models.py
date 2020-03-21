from django.db import models

from django.contrib.auth.models import User


# HELPER

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('0', 'Sonstiges'),
        ('1', 'Lebensmittel'),
        ('2', 'Getränke'),
        ('3', 'Kleidung'),
        ('4', 'Schuhe'),
        ('5', 'Drogerie'),
        ('6', 'Optiker'),
        ('7', 'Haushaltswaren'),
        ('8', 'Elektronikwaren'),
        ('9', 'Outdoor & Sport'),
        ('10', 'Kunst & Musik'),
        ('11', 'Schreibwaren'),
        ('12', 'Geschenke'),
        ('13', 'Wäscherei'),
        ('14', 'Tabakwaren'),
        ('15', 'Spielzeugwaren'),
    ]
    categories = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='0')
    icon = models.ImageField()


class Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)


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
    gps_position = models.ForeignKey('Location', on_delete=models.CASCADE, default=None, blank=True, null=True)

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
    shop_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    gps_position = models.ForeignKey('Location', on_delete=models.CASCADE, default=None, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loaded = models.DateTimeField(blank=True, null=True)
    delivered = models.DateTimeField(blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    transaction_content = models.CharField(max_length=600)

    def __str__(self):
        return self.transaction_content
