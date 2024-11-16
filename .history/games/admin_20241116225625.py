from django.contrib import admin
from .models import Game, Review

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'rating', 'created_at')
    search_fields = ('user__email', 'game__title')
