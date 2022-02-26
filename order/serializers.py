from importlib.metadata import requires
from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Order, OrderDetail
from product.serializers import *


class OrderDetailBasicSerializer(serializers.ModelSerializer):

    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['product', 'product_detail', 'quantity',]

class OrderDetailSerializer(serializers.ModelSerializer):
    
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['id','order', 'product', 'product_detail', 'quantity',]


class OrderSerializer(serializers.ModelSerializer):
    
    buyer_detail = UserSerializer(source='buyer', read_only=True)
    order_items_detail = OrderDetailBasicSerializer(source='order_items',many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id','order_number', 'buyer', 'buyer_detail','order_items', 'order_items_detail','status', 'is_paid', 'date_time']