from django.urls import include, path
from rest_framework import routers

from shop import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'seller', views.SellerViewSet)
router.register(r'buyer', views.BuyerViewSet)
router.register(r'driver', views.DriverViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
