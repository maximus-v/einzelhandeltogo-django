from django.contrib import admin

from shop.models import Seller, Buyer, Driver, Transaction

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Driver)
admin.site.register(Transaction)
