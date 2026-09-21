from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Favorite


def catalog(request):
    products = Product.objects.select_related("category").prefetch_related("images").all()

    query = request.GET.get("q", "").strip()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    cat_slug = request.GET.get("categorie", "")
    if cat_slug:
        products = products.filter(category__slug=cat_slug)

    prix = request.GET.get("prix", "")
    if prix == "moins15":
        products = products.filter(price__lt=15000)
    elif prix == "15a25":
        products = products.filter(price__gte=15000, price__lte=25000)
    elif prix == "plus25":
        products = products.filter(price__gt=25000)

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = list(Favorite.objects.filter(user=request.user).values_list("product_id", flat=True))

    context = {
        "products": products,
        "categories": Category.objects.all(),
        "query": query,
        "selected_categorie": cat_slug,
        "selected_prix": prix,
        "favorite_ids": favorite_ids,
    }
    return render(request, "products/catalog.html", context)


def detail(request, slug):
    product = get_object_or_404(Product.objects.prefetch_related("images"), slug=slug)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
    related = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    context = {"product": product, "is_favorite": is_favorite, "related": related}
    return render(request, "products/detail.html", context)


@login_required
def toggle_favorite(request, slug):
    product = get_object_or_404(Product, slug=slug)
    fav, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if not created:
        fav.delete()
        messages.info(request, "Produit retiré de vos favoris.")
    else:
        messages.success(request, "Produit ajouté à vos favoris.")
    return redirect(request.META.get("HTTP_REFERER", "products:catalog"))


@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related("product")
    return render(request, "products/favorites.html", {"favorites": favorites})
