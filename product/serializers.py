from rest_framework import serializers
from .models import Product, Category
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for categories that serialize all of the fields
    based on Category model
    """

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer for products that serialize:
    (id', 'url', "name", "slug", "category", "price", "available",
    "stock", "created", "image", "description")
    and add relation to category serializer \nbased on Product model
    """

    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'url', "name", "slug", "category", "price",
            "available", "stock", "created", "updated","image", "description")