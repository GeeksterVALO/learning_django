from django.urls import path
from .views import ArticleIndexView

urlpatterns = [
    path('', ArticleIndexView.as_view(), name='article_index'),
]