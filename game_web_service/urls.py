from django.contrib import admin
from django.urls import path, include
from game_web_service import views

from game_web_service.views import indexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', include('game_web_service.article.urls')),
    path('admin/', admin.site.urls),
]
