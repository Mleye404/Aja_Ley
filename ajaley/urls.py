from django.contrib import admin
import ajaley.admin_site  # noqa
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from products.api import ProductViewSet
from core.views import set_language_custom

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("langue/", set_language_custom, name="set_language"),
    path("api/", include(router.urls)),
    path("", include("core.urls")),
    path("boutique/", include("products.urls")),
    path("panier/", include("cart.urls")),
    path("commandes/", include("orders.urls")),
    path("paiement/", include("payments.urls")),
    path("compte/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")
