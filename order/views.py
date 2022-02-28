from itertools import product
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions, status, exceptions

from .serializers import (
    OrderDetailSerializer,
    OrderSerializer,
    OrderDetailBasicSerializer
)
from .models import Order, OrderDetail
from .models import Product

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('buyer', 'order_items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [
        permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number']

    def get_queryset(self):
        user = self.request.user
        return Order.objects.prefetch_related('buyer','order_items__product').filter(buyer=user)

    def list(self, request):
        order_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": order_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.select_related('order', 'product').all()
    serializer_class = OrderDetailSerializer
    permission_classes = [
        permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['order', 'product']

    def get_queryset(self):
        user = self.request.user
        return OrderDetail.objects.select_related('order__buyer', 'product').filter(order__buyer=user)

    def list(self, request):
        orderdetail_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "rows": orderdetail_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_quantity = serializer.validated_data['quantity']

        product = Product.objects.filter(
            id=str(serializer.validated_data['product'])
        ).order_by('created').first()

        if product and product.stock >= order_quantity:
            actual_quantity = product.stock
            product.stock = actual_quantity - order_quantity
            product.save(update_fields=['stock'])
            serializer.save()
        else:
            raise exceptions.NotAcceptable("Quantity of this product is out.")

        try:
            order_number = request.data.get("order_number", "")
            quantity = request.data.get("quantity", 1)
        except:
            pass

        try:
            order = Order.objects.get(buyer=self.request.user)
        except ObjectDoesNotExist:
            order = Order().create_order(self.request.user, order_number)

        #total = quantity * product.price
        
        order_item = OrderDetail().create_order_item(order, product, quantity)
        serializer = OrderDetailBasicSerializer(order_item)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
