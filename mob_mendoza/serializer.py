from rest_framework import serializers
from .models import Forniture, Product, Client, Address, ShoppingCart, PurchaseOrder, DetailedOrder, CartItem

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

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ['id', 'client', 'created_at', 'items']

class DetailedOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = DetailedOrder
        fields = ['id', 'product', 'quantity', 'cost']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    details = DetailedOrderSerializer(many=True)
    
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'client', 'created_at', 'status', 'details']

class OrderCreateSerializer(serializers.ModelSerializer):
    details = DetailedOrderSerializer(many=True)

    class Meta:
        model = PurchaseOrder
        fields = ['customer', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        order = PurchaseOrder.objects.create(**validated_data)
        for detail_data in details_data:
            product = Product.objects.get(id=detail_data['product']['id'])
            DetailedOrder.objects.create(order=order, product = product, **detail_data)
        return order

