from django.urls import path

from game_web_service.article import views

urlpatterns = [
    path('', ArticleIndexView.as_view(), name='articlex_index'),
]