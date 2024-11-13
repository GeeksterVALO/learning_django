from django.urls import path

from game_web_service.article import views

urlpatterns = [
    path('', views.index, name='article_index'),
]