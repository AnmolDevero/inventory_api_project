from django.urls import path, include
from rest_framework.routers import DefaultRouter



# APIView imports
from .views import (ProductListCreateView, ProductDetailView,
                    signup_api, delete_acount_api, ChangePasswordView)

# Mixin views imports
from .mixin_views import (ProductListCreateMixinView, ProductRetrieveUpdateDestroyMixinView,
                          SignupView, DeleteAccountView,ChangePasswordView as MChangePasswordView)
                          

# Generic views imports
from .generic_views import (ProductListCreateView as GProductListCreateView,ProductRetrieveUpdateDestroyView,
                            SignupView as GSignupView, DeleteAccountView as GDeleteAccountView, 
                            ChangePasswordView as GChangePasswordView)

# ViewSet imports
from .viewset_views import ProductViewSet,SignupViewSet,ChangePasswordViewSet


# Router for viewset
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'users', SignupViewSet, basename='signup')
router.register(r'change-password', ChangePasswordViewSet, basename='change-password')



urlpatterns = [
    # APIView URLs
    path('api/products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('api/product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/signup/', signup_api, name='signup'),
    path('api/delete-acount/', delete_acount_api, name='delete_acount'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
    
    # MixinView URLs
    path('m/products/', ProductListCreateMixinView.as_view(), name='mixin_list_create'),
    path('m/product/<int:pk>/', ProductRetrieveUpdateDestroyMixinView.as_view(), name='mixin_retrieve_update_destroy'),
    path('m/signup/', SignupView.as_view(), name='mixin_signup'),
    path('m/delete-account/', DeleteAccountView.as_view, name='mixin_delete_account'),
    path('m/change-password/', MChangePasswordView.as_view(), name='mixin_change_password'),

    # GenericView URLs
    path('g/products/', GProductListCreateView.as_view(), name='g_list_create'),
    path('g/product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='g_retrieve_update_destroy'),
    path('g/signup/', GSignupView.as_view(), name='g_ignup'),
    path('g/delete-account/', GDeleteAccountView.as_view, name='g_delete_account'),
    path('g/change-password/', GChangePasswordView.as_view(), name='g_change_password'),
    
    # ViewSet URLs
    path('v/', include(router.urls)),
]



