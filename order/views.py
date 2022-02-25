from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions, status, exceptions

from .serializers import (
    OrderDetailSerializer,
    OrderSerializer,
)
from .models import Order, OrderDetail
from .models import Product

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('buyer').all()
    serializer_class = OrderSerializer
    permission_classes = [
        permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number']


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.select_related('order', 'product').all()
    serializer_class = OrderDetailSerializer
    permission_classes = [
        permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['order', 'product']