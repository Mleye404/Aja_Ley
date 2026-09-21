from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum, Count
from orders.models import Order
from products.models import Product
from django.contrib.auth.models import User


@staff_member_required
def dashboard_home(request):
    orders = Order.objects.all()
    context = {
        "total_orders": orders.count(),
        "pending_orders": orders.filter(status="pending_payment").count(),
        "preparing_orders": orders.filter(status="preparing").count(),
        "delivered_orders": orders.filter(status="delivered").count(),
        "total_customers": User.objects.filter(is_staff=False).count(),
        "total_products": Product.objects.count(),
        "revenue": orders.filter(status__in=["paid", "confirmed", "preparing", "ready", "shipping", "delivered"]).aggregate(s=Sum("total"))["s"] or 0,
        "recent_orders": orders.order_by("-created_at")[:8],
        "status_breakdown": orders.values("status").annotate(count=Count("id")),
    }
    return render(request, "dashboard/home.html", context)
