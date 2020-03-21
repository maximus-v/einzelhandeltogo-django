from django.contrib.auth.models import User

from rest_framework import viewsets, permissions

from shop.serializers import UserSerializer, SellerSerializer, BuyerSerializer, DriverSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SellerViewSet(viewsets.ModelViewSet):
    # queryset = Seller.objects.all()
    queryset = User.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuyerViewSet(viewsets.ModelViewSet):
    # queryset = Buyer.objects.all()
    queryset = User.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticated]


class DriverViewSet(viewsets.ModelViewSet):
    # queryset = Driver.objects.all()
    queryset = User.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
