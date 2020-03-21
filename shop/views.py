from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from shop.models import Seller, Buyer, Driver, Category, Address, Product, Location, Transaction
from shop.serializers import UserSerializer, SellerSerializer, BuyerSerializer, DriverSerializer, \
    ShopCategorySerializer, AddressSerializer, ProductSerializer, LocationSerializer, TransactionSerializer, \
    UserProfileSerializer


# Following views / endpoints must be implemented
# TODO GET profiles of user
# TODO GET list of driver's transactions
# TODO GET list of buyer's transactions
# TODO GET list of seller's transactions
# TODO GET location of driver
# TODO GET address of buyer
# TODO GET address of seller


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


@api_view(['GET'])
def profile_list(request, user_id):
    user = User.objects.get(pk=user_id)
    response_data = dict()
    if hasattr(user, 'seller'):
        response_data["seller"] = SellerSerializer(user.seller).data
    else:
        response_data["seller"] = {}
    if hasattr(user, 'buyer'):
        response_data["buyer"] = BuyerSerializer(user.buyer).data
    else:
        response_data["buyer"] = {}
    if hasattr(user, 'driver'):
        response_data["driver"] = DriverSerializer(user.driver).data
    else:
        response_data["driver"] = {}
    return Response(response_data, status=status.HTTP_200_OK)


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
    authentication_classes = [TokenAuthentication, BasicAuthentication]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ShopCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ShopCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]