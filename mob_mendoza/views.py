from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import Forniture

# Create your views here.
class MobiliarioView(viewsets.ModelViewSet):
    serializer_class = FornitureSerializer
    queryset = Forniture.objects.all()

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderDetailedView(viewsets.ModelViewSet):
    serializer_class = OrderDetailedSerializer
    queryset = OrderDetail.objects.all()

class OrderListView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerComplete