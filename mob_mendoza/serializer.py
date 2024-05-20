from rest_framework import serializers
from .models import Forniture, Product, Client, Address, ShoppingCart, PurchaseOrder, DetailedOrder

class FornitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forniture
        # fields = ('id', 'tipo')
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class DetailedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedOrder
        fields = '__all__'

