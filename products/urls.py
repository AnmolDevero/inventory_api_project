from django.urls import path, include
from rest_framework.routers import DefaultRouter

# APIView imports
from .views import (
    ProductListCreateView, ProductDetailView,signup_api, delete_acount_api, ChangePasswordView)

# Mixin views imports
from .mixin_views import (ProductListCreateMixinView, ProductRetrieveUpdateDestroyMixinView)

# Generic views imports
from .generic_views import ProductListCreateView as GProductListCreateView,ProductRetrieveUpdateDestroyView

# ViewSet imports
from .viewset_views import ProductViewSet


# Router for viewset
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    # APIView URLs
    path('api/products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/signup/', signup_api, name='signup'),
    path('api/delete/acount/', delete_acount_api, name='delete_acount'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
    
    # MixinView URLs
    path('m/products/', ProductListCreateMixinView.as_view(), name='mixin_list_create'),
    path('m/product/<int:pk>/', ProductRetrieveUpdateDestroyMixinView.as_view(), name='mixin_retrieve_update_destroy'),

    # GenericView URLs
    path('g/products/', GProductListCreateView.as_view(), name='list_create'),
    path('g/product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy'),

    # ViewSet URLs
    path("v/", include(router.urls)),
]



