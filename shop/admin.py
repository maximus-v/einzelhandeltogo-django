from django.contrib import admin

from shop.models import Seller, Buyer, Driver, Transaction, Location, Address

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Driver)
admin.site.register(Transaction)
admin.site.register(Location)
admin.site.register(Address)
