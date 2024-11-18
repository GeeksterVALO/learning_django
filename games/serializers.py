from rest_framework import serializers
from .models import Game, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'logo', 'download_link', 'purchase_link', 'rating', 'categories']