from django.shortcuts import render
from rest_framework import viewsets
from .serializer import FornitureSerializer, ProductSerializer, ClientSerializer, AddressSerializer, ShoppingCartSerializer, PurchaseOrderSerializer, DetailedOrderSerializer
from .models import Forniture, Product, Client, Address, ShoppingCart, PurchaseOrder, DetailedOrder

# Create your views here.
class MobiliarioView(viewsets.ModelViewSet):
    serializer_class = FornitureSerializer
    queryset = Forniture.objects.all()

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class ShoppingCartView(viewsets.ModelViewSet):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()

class PurchaseOrderView(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()

class DetailedOrderView(viewsets.ModelViewSet):
    serializer_class = DetailedOrderSerializer
    queryset = DetailedOrder.objects.all()
    
