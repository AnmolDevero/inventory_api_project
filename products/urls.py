from django.urls import path
from .views import ProductListCreateView,ProductDetailView,signup_api,delete_acount_api,ChangePasswordView


urlpatterns = [
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='prduct-detail'),
    path('api/signup/', signup_api, name='signup'),
    path('api/delete/acount/', delete_acount_api, name='delete_acount'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
]