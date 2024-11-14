# game_web_service/article/models.py
from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

print(article.id, article.name, article.body, article.created_at, article.updated_at)