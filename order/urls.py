from django.urls import path, include
from rest_framework import routers
from order.views import OrderViewSet, OrderDetailViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'orders_detail', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]