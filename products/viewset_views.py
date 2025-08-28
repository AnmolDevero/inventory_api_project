from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer,SignupSerializer,ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from django.contrib.auth.password_validation import validate_password



class ProductViewSet(ModelViewSet):
    
    serializer_class = ProductSerializer

    filterset_fields = ['in_stock', 'user']  
    search_fields = ['name']  
    ordering_fields = ['price', 'added_on']  
    ordering = ['-added_on']  

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SignupViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def delete_account(self, request):
        request.user.delete()
        return Response({"message": "Account deleted successfully"}, status=204)
    

class ChangePasswordViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['put'], url_name='')
    def change_password(self, request):
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










