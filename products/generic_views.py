from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,GenericAPIView
from .models import Product
from .serializers import ProductSerializer,SignupSerializer,ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from django.contrib.auth.password_validation import validate_password



class ProductListCreateView(ListCreateAPIView):
    
    serializer_class = ProductSerializer
 
    filterset_fields = ['in_stock']  
    search_fields = ['name']  
    ordering_fields = ['price', 'added_on']  
    ordering = ['-added_on']  

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)



class SignupView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer



class DeleteAccountView(GenericAPIView):

    def delete(self, request, *args, **kwargs):
        request.user.delete()
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





    

