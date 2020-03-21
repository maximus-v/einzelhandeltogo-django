from django.urls import include, path
from rest_framework import routers

from shop import views
from rest_framework.authtoken import views as at_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'sellers', views.SellerViewSet, basename='sellers')
router.register(r'buyers', views.BuyerViewSet, basename='buyers')
router.register(r'drivers', views.DriverViewSet, basename='drivers')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', at_views.obtain_auth_token)
]
