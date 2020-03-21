from django.contrib.auth.models import User
from rest_framework import serializers

from shop.models import Seller, Buyer, Driver, Transaction, Address, Product, Location


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class UserProfileSerializer(serializers.Serializer):
    seller = serializers.SerializerMethodField('get_seller')
    # buyer = serializers.SerializerMethodField('get_buyer')
    # driver = serializers.SerializerMethodField('get_driver')

    def __init__(self, *args, **kwargs):
        print("Init called")
        context = kwargs.pop('context')
        self.user_id = context.get('user_id')
        print(self.user_id)
        super(UserProfileSerializer, self).__init__(*args, **kwargs)

    def get_seller(self, obj):
        print("Get seller")
        return SellerSerializer(Seller.objects.filter(user=self.user_id)).data


class TransactionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        transaction = Transaction.objects.create(
            transaction_content=validated_data['transaction_content'],
            seller=validated_data['seller'],
            buyer=validated_data['buyer']
        )

        transaction.driver = get_closest_driver()
        transaction.save()

        return transaction

    class Meta:
        model = Transaction
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


def get_closest_driver():
    # TODO this method should return the nearest available driver
    return Driver.objects.first()
