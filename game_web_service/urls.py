# game_web_service/urls.py
from django.contrib import admin
from django.urls import path, include
from game_web_service.article.views import ArticleIndexView, IndexView, article_detail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', ArticleIndexView.as_view(), name='article_index'),
    path('articles/<str:tags>/<int:article_id>/', article_detail, name='article'),
    path('admin/', admin.site.urls),
]
