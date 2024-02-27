from django.shortcuts import render
from rest_framework import viewsets
from .serializer import FornitureSerializer, ProductSerializer
from .models import Forniture, Product

# Create your views here.
class MobiliarioView(viewsets.ModelViewSet):
    serializer_class = FornitureSerializer
    queryset = Forniture.objects.all()

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    
