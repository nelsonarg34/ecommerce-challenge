from itertools import product
from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Order, OrderDetail
from product.serializers import *


class OrderDetailBasicSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['order', 'product', 'product_detail', 'quantity',]


class OrderDetailBasicV1Serializer(serializers.ModelSerializer):
    product_detail = ProductBasicSerializer(source='product', read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['product', 'product_detail', 'quantity',]


class OrderSerializer(serializers.ModelSerializer):
    buyer_detail = UserSerializer(source='buyer', read_only=True)
    order_items_detail = OrderDetailBasicV1Serializer(source='order_items',many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'buyer', 'buyer_detail', 'order_items_detail','status', 'is_paid', 'date_time']


class OrderBasicSerializer(serializers.ModelSerializer):
    buyer_detail = UserSerializer(source='buyer', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'buyer_detail', 'status', 'is_paid', 'date_time']


class OrderDetailSerializer(serializers.ModelSerializer):
    product_detail = ProductBasicSerializer(source='product', read_only=True)
    order_detail = OrderBasicSerializer(source='order', read_only=True)
    order = OrderBasicSerializer(required=False, read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['id','order', 'order_detail', 'product', 'product_detail', 'quantity',]



