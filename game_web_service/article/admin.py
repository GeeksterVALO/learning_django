from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at')
    list_filter = ('created_at', 'id')
    search_fields = ['name', 'body']