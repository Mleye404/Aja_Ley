from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from cart.utils import get_or_create_cart
from .forms import CheckoutForm
from .models import Order, OrderItem, ShippingRate


def compute_shipping(country, city):
    if country.strip().lower() not in ["sénégal", "senegal"]:
        return 0, "Livraison internationale — devis personnalisé. Contactez-nous sur WhatsApp."
    city_norm = city.strip().lower()
    if "thi" in city_norm and "es" in city_norm:
        return settings.SHIPPING_THIES, ""
    if "dakar" in city_norm:
        return settings.SHIPPING_DAKAR, ""
    rate = ShippingRate.objects.filter(city__iexact=city.strip()).first()
    if rate:
        return rate.fee, ""
    return 0, "Frais de livraison à confirmer avec AJA LEY."


def checkout(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related("product")
    if not items.exists():
        messages.warning(request, "Votre panier est vide.")
        return redirect("cart:view_cart")

    initial = {}
    if request.user.is_authenticated:
        initial = {"first_name": request.user.first_name, "last_name": request.user.last_name,
                   "email": request.user.email}

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fee, note = compute_shipping(data["country"], data["city"])
            subtotal = cart.subtotal

            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                first_name=data["first_name"], last_name=data["last_name"],
                phone=data["phone"], email=data["email"],
                country=data["country"], city=data["city"], district=data["district"],
                full_address=data["full_address"], postal_code=data["postal_code"],
                extra_info=data["extra_info"],
                shipping_fee=fee, shipping_note=note,
                subtotal=subtotal, total=subtotal + fee,
            )
            for item in items:
                OrderItem.objects.create(
                    order=order, product=item.product, product_name=item.product.name,
                    unit_price=item.product.price, quantity=item.quantity,
                    bust=item.bust, waist=item.waist, hips=item.hips, shoulders=item.shoulders,
                    desired_length=item.desired_length, sleeve_length=item.sleeve_length,
                    extra_notes=item.extra_notes,
                )
            cart.is_ordered = True
            cart.save()
            return redirect("payments:choose", reference=order.reference)
    else:
        form = CheckoutForm(initial=initial)

    return render(request, "orders/checkout.html", {"form": form, "cart": cart, "items": items})


def confirmation(request, reference):
    order = get_object_or_404(Order.objects.prefetch_related("items"), reference=reference)
    return render(request, "orders/confirmation.html", {"order": order})
