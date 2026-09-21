from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import CartItem
from .forms import MeasurementForm
from .utils import get_or_create_cart


def add_to_cart(request, slug):
    """Étape 1 : la cliente clique sur 'Ajouter au panier' -> on l'envoie
    vers le formulaire de mensurations avant tout ajout réel."""
    product = get_object_or_404(Product, slug=slug)
    if not product.is_available:
        messages.error(request, "Ce produit est actuellement en rupture de stock.")
        return redirect(product.get_absolute_url())
    return redirect("cart:measurements", slug=slug)


def measurements(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            cart = get_or_create_cart(request)
            item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={"quantity": 1})
            if not created:
                item.quantity += 1
            for field in ["bust", "waist", "hips", "shoulders", "desired_length", "sleeve_length", "extra_notes"]:
                setattr(item, field, form.cleaned_data[field])
            item.save()
            messages.success(request, f"« {product.name} » a été ajouté à votre panier avec vos mensurations.")
            return redirect("cart:view_cart")
    else:
        form = MeasurementForm()
    return render(request, "cart/measurements.html", {"form": form, "product": product})


def view_cart(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related("product").prefetch_related("product__images")
    return render(request, "cart/cart.html", {"cart": cart, "items": items})


def update_quantity(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    action = request.POST.get("action")
    if action == "increase":
        item.quantity += 1
        item.save()
    elif action == "decrease":
        item.quantity -= 1
        if item.quantity <= 0:
            item.delete()
        else:
            item.save()
    return redirect("cart:view_cart")


def remove_item(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    messages.info(request, "Produit retiré du panier.")
    return redirect("cart:view_cart")


def edit_measurements(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    if request.method == "POST":
        form = MeasurementForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensurations mises à jour.")
            return redirect("cart:view_cart")
    else:
        form = MeasurementForm(instance=item)
    return render(request, "cart/measurements.html", {"form": form, "product": item.product, "editing": True, "item": item})
