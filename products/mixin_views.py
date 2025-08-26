# mixin_views.py
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .models import Product
from .serializers import ProductSerializer



class ProductListCreateMixinView(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class ProductRetrieveUpdateDestroyMixinView(mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,
                                            mixins.DestroyModelMixin,
                                            GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

