from django.urls import path
#from .views import ArticleIndexView
from game_web_service.article.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]