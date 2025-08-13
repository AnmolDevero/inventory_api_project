from django.urls import path
from .views import ProductListCreateView, ProductDetailView,SignupView


urlpatterns = [
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='prduct-detail'),
    path('api/signup/', SignupView.as_view(), name='signup')
]