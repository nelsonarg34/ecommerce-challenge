from django.contrib import admin
from .models import Order, OrderDetail

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'order_number', "status", "is_paid", "buyer", "date_time")

    search_fields = ("order_name", "status", "buyer")
    date_hierarchy = "date_time"
    list_editable = ["status"]


@admin.register(OrderDetail)
class OrerDetailAdmin(admin.ModelAdmin):

    list_display = ("order", "product", "quantity", "created", "updated")
    list_editable = ["quantity"]
