# game_web_service/urls.py
from django.contrib import admin
from django.urls import path, include
from game_web_service.article.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', include('game_web_service.article.urls')),
    path('admin/', admin.site.urls),
]
