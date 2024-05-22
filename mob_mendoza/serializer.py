from rest_framework import serializers
from .models import Forniture, Customer, Product, Cart, Address, Order, OrderDetail

class FornitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forniture        
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializerComplete(serializers.ModelSerializer):
    customer = CustomerSerializer()
    address = AddressSerializer()
    order_details = OrderDetailedSerializer(many=True, source='orderdetail_set')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'total', 'address', 'deadline', 'order_details']
