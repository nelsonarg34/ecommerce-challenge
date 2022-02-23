from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = "modified"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = "modified"


class OrderItemMiniSerializer(serializers.ModelSerializer):
    order = OrderSerializer(required=False, read_only=True)
    product = ProductSerializer(required=False, read_only=True)

    class Meta:
        model = OrderItem
        exclude = "modified"