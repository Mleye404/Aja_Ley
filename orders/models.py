import random
import string
from django.db import models
from django.conf import settings
from products.models import Product


def generate_order_reference():
    return "AJA-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))


class ShippingRate(models.Model):
    """Frais de livraison administrables depuis Django Admin."""
    city = models.CharField("Ville", max_length=100, unique=True)
    fee = models.PositiveIntegerField("Frais (FCFA)")

    class Meta:
        verbose_name = "Frais de livraison"
        verbose_name_plural = "Frais de livraison"

    def __str__(self):
        return f"{self.city} — {self.fee} FCFA"


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending_payment", "En attente de paiement"),
        ("paid", "Paiement confirmé"),
        ("confirmed", "Commande confirmée"),
        ("preparing", "En préparation"),
        ("ready", "Prête"),
        ("shipping", "En livraison"),
        ("delivered", "Livrée"),
        ("cancelled", "Annulée"),
    ]

    reference = models.CharField(max_length=20, unique=True, default=generate_order_reference)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")

    # Informations cliente (toujours renseignées, même en invitée)
    first_name = models.CharField("Prénom", max_length=80)
    last_name = models.CharField("Nom", max_length=80)
    phone = models.CharField("Téléphone", max_length=30)
    email = models.EmailField("Email", blank=True)

    # Adresse de livraison
    country = models.CharField("Pays", max_length=100, default="Sénégal")
    city = models.CharField("Ville", max_length=100)
    district = models.CharField("Quartier", max_length=100, blank=True)
    full_address = models.TextField("Adresse complète")
    postal_code = models.CharField("Code postal", max_length=20, blank=True)
    extra_info = models.CharField("Indication complémentaire", max_length=255, blank=True)

    shipping_fee = models.PositiveIntegerField("Frais de livraison (FCFA)", default=0)
    shipping_note = models.CharField("Note livraison", max_length=255, blank=True)
    subtotal = models.PositiveIntegerField("Sous-total (FCFA)", default=0)
    total = models.PositiveIntegerField("Total (FCFA)", default=0)

    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default="pending_payment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Commande {self.reference}"

    @property
    def is_international(self):
        return self.country.strip().lower() not in ["sénégal", "senegal"]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="order_items")
    product_name = models.CharField(max_length=150)
    unit_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    # Mensurations figées au moment de la commande
    bust = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    hips = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    shoulders = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    desired_length = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    extra_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Article de commande"
        verbose_name_plural = "Articles de commande"

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"

    @property
    def line_total(self):
        return self.unit_price * self.quantity
