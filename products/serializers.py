from rest_framework import serializers
from .models import Product, ProductImage, Category


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "order"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "category", "description", "price",
                  "color", "is_available", "is_featured", "is_new", "images"]
