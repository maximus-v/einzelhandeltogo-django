from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView

from shop.models import Seller, Buyer, Driver
from shop.serializers import UserSerializer, SellerSerializer, BuyerSerializer, DriverSerializer


# Following views / endpoints must be implemented
# TODO POST register as user
# TODO GET list of driver's transactions
# TODO GET list of buyer's transactions
# TODO GET list of seller's transactions
# TODO GET transaction details
# TODO POST new transaction
# TODO UPDATE existing transaction
# TODO DELETE transaction
# TODO POST login with credentials


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

