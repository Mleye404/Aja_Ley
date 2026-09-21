from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST
from django.utils import translation
from django.shortcuts import redirect
from products.models import Product, Category


def home(request):
    featured = Product.objects.filter(is_featured=True)[:5]
    new_arrivals = Product.objects.filter(is_new=True)[:5]
    if not featured.exists():
        featured = Product.objects.all()[:5]
    if not new_arrivals.exists():
        new_arrivals = Product.objects.all()[:5]
    categories = Category.objects.all()[:4]
    context = {"featured": featured, "new_arrivals": new_arrivals, "categories": categories}
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def set_language_custom(request):
    lang = request.GET.get("lang", "fr")
    next_url = request.GET.get("next", "/")
    translation.activate(lang)
    response = redirect(next_url)
    response.set_cookie(settings_lang_cookie(), lang)
    return response


def settings_lang_cookie():
    from django.conf import settings
    return settings.LANGUAGE_COOKIE_NAME if hasattr(settings, "LANGUAGE_COOKIE_NAME") else "django_language"
