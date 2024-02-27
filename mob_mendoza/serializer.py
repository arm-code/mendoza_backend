from rest_framework import serializers
from .models import Forniture, Product

class FornitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forniture
        # fields = ('id', 'tipo')
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'