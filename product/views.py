from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer



# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticated]
    print(queryset)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)

    
class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)