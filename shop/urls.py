from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from shop import views
from rest_framework.authtoken import views as at_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'sellers', views.SellerViewSet, basename='sellers')
router.register(r'buyers', views.BuyerViewSet, basename='buyers')
router.register(r'drivers', views.DriverViewSet, basename='drivers')
router.register(r'categories', views.ShopCategoryViewSet, basename='categories')
router.register(r'addresses', views.AddressViewSet, basename='addresses')
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'locations', views.LocationViewSet, basename='locations')


schema_view = get_schema_view(
    openapi.Info(
        title="ETG API",
        default_version="v1",
        description="Description of the fundamental API of the middleware",
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.CreateUserView),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', at_views.obtain_auth_token),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
