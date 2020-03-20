from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Seller
        model = User
        fields = ['id', 'username', 'email', 'groups']


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Buyer
        model = User
        fields = ['id', 'username', 'email', 'groups']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Driver
        model = User
        fields = ['id', 'username', 'email', 'groups']