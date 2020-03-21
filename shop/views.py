from django.contrib.auth.models import User

from rest_framework import viewsets, permissions

from shop.models import Seller, Buyer, Driver
from shop.serializers import UserSerializer, SellerSerializer, BuyerSerializer, DriverSerializer


# Following views / endpoints must be implemented
# TODO GET list of buyers
# TODO GET buyer details
# TODO POST register as buyer
# TODO UPDATE buyer profile
# TODO DELETE buyer profile
# TODO GET list of sellers
# TODO GET seller details
# TODO POST register as seller
# TODO UPDATE seller profile
# TODO DELETE seller profile
# TODO GET list of drivers
# TODO GET driver details
# TODO POST register as driver
# TODO UPDATE driver profile
# TODO DELETE driver profile
# TODO GET list of driver's transactions
# TODO GET list of buyer's transactions
# TODO GET list of seller's transactions
# TODO GET transaction details
# TODO POST new transaction
# TODO UPDATE existing transaction
# TODO DELETE transaction
# TODO POST login with credentials


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticated]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
