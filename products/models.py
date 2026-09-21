from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


class Category(models.Model):
    name = models.CharField("Nom", max_length=100)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Image", upload_to="categories/", blank=True, null=True)
    order = models.PositiveIntegerField("Ordre", default=0)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:catalog") + f"?categorie={self.slug}"


class Product(models.Model):
    name = models.CharField("Nom", max_length=150)
    slug = models.SlugField("Slug", unique=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Catégorie", on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name="products")
    description = models.TextField("Description", blank=True)
    price = models.PositiveIntegerField("Prix (FCFA)")
    color = models.CharField("Couleur", max_length=100, blank=True)
    is_available = models.BooleanField("Disponible", default=True)
    is_featured = models.BooleanField("Mis en avant", default=False)
    is_new = models.BooleanField("Nouveau", default=False)
    created_at = models.DateTimeField("Créé le", auto_now_add=True)
    updated_at = models.DateTimeField("Mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            i = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:detail", args=[self.slug])

    @property
    def main_image(self):
        img = self.images.order_by("order").first()
        return img.image.url if img else ""


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Photo", upload_to="products/")
    order = models.PositiveIntegerField("Ordre", default=0)

    class Meta:
        verbose_name = "Photo produit"
        verbose_name_plural = "Photos produit"
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.product.name} - photo {self.order + 1}"


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favori"
        verbose_name_plural = "Favoris"
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user} ♥ {self.product}"
