from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .models import Product
from .serializers import ProductSerializer,SignupSerializer,ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from django.contrib.auth.password_validation import validate_password




class ProductListCreateMixinView(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 GenericAPIView):

    serializer_class = ProductSerializer
   
    filterset_fields = ['in_stock']  
    search_fields = ['name']  
    ordering_fields = ['price', 'added_on']  
    ordering = ['-added_on']                

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    



class ProductRetrieveUpdateDestroyMixinView(mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,
                                            mixins.DestroyModelMixin,
                                            GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class SignupView(mixins.CreateModelMixin,GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class DeleteAccountView(GenericAPIView):

    def delete(self, request, *args, **kwargs):
        user = request.user 
        user.delete()
        return Response({"message": "Account deleted successfully"})
    


class ChangePasswordView(GenericAPIView):
    
    def put(self, request):
    
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not user.check_password(old_password):
                return Response({"old_password": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                validate_password(new_password, user)
            except Exception as e:
                return Response({"new_password": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




