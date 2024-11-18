from rest_framework import serializers
from .models import CatalogItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class CatalogItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = CatalogItem
        fields = ['id', 'title', 'description', 'logo', 'rating', 'categories']