from django.shortcuts import render,redirect

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .serializers import ChangePasswordSerializer



class ProductListCreateView(APIView): # class-based view for listing and creating products
    # Read
    def get(self, request):
        get_products = Product.objects.filter(user=request.user)

        paginator = PageNumberPagination()
        paginator.page_size = 3
        products = paginator.paginate_queryset(get_products, request)

        search = request.query_params.get('search', None)
        if search:
            products = products.filter(name__icontains=search)

        serializer = ProductSerializer(products, many=True)
        return Response (serializer.data)
    # Create
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetailView(APIView):

    def get_object(self, pk, user):  # helper function to fetch object by ID.
        try:
            return Product.objects.get(pk=pk, user=user)
        except Product.DoesNotExist:
            return None
    # Filter  
    def get(self, request, pk):
        product = self.get_object(pk, user=request.user) # Call the get_object() method and pass the 'pk' (perameter) received from the request URL.  
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    # Update
    def put(self, request, pk):
        product = self.get_object(pk, user=request.user)
        if not product:
            return Response ({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        product = self.get_object(pk, user=request.user)
        if not product:
            return Response ({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    def delete(self, request, pk):
        product = self.get_object(pk,user=request.user)
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
     
    
@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response ({'error':'name and password required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response ({'error':'user already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) < 6:
        return Response({'error': 'Password is too short'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user (username=username, password=password)
    return Response ({'message':'user created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def delete_acount_api(request):
    request.user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 



class ChangePasswordView(APIView):
    
    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not user.check_password(old_password):
                return Response ({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

