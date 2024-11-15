# game_web_service/urls.py
from django.contrib import admin
from django.urls import path, include
from game_web_service.article.views import IndexView, ArticleView, ArticleCommentsView, article_detail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', IndexView.as_view(), name='article_index'),
    path('articles/tagged/<str:tags>/<int:article_id>/', article_detail, name='article'),
    path('articles/<int:id>/', ArticleView.as_view(), name='article_detail'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view(), name='article_comments'),
    path('admin/', admin.site.urls),
]
