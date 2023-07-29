from rest_framework import serializers
from .models import Product, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Stock
        fields = "__all__"
        extra_kwargs = {"cost": {"required": False}}
