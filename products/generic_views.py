from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer




class ProductListCreateView(ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer









