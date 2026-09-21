from django.contrib import admin
from .models import Order, OrderItem, ShippingRate


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "unit_price", "quantity", "bust", "waist", "hips",
                        "shoulders", "desired_length", "sleeve_length", "extra_notes")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("reference", "full_name", "city", "country", "total", "status", "created_at")
    list_filter = ("status", "country", "city")
    search_fields = ("reference", "first_name", "last_name", "phone", "email")
    list_editable = ("status",)
    inlines = [OrderItemInline]


@admin.register(ShippingRate)
class ShippingRateAdmin(admin.ModelAdmin):
    list_display = ("city", "fee")
