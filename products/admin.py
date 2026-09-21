from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, Favorite


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "order", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.pk and obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image.url)
        return "—"
    preview.short_description = "Aperçu"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available", "is_featured", "is_new", "photo_count")
    list_filter = ("category", "is_available", "is_featured", "is_new")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]
    list_editable = ("is_available", "is_featured", "is_new")

    def photo_count(self, obj):
        return obj.images.count()
    photo_count.short_description = "Photos"


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "created_at")
