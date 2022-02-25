from importlib.metadata import requires
from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Order, OrderDetail
from product.serializers import *


class OrderDetailSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(required=False, read_only=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderDetailBasicSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(required=False, read_only=True)

    class Meta:
        model = OrderDetail
        exclude = ('order', )


class OrderSerializer(serializers.ModelSerializer):

    buyer = UserSerializer(required=False, read_only=True)
    order_items = OrderDetailBasicSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id','order_number', 'buyer', 'order_items', 'status', 'is_paid', 'date_time']