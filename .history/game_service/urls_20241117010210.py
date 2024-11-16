from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('games/', include('games.urls')),
    path('catalog/', include('catalog.urls')),
    path('news/', include('news.urls')),
    path('', catalog_views.home, name='home'),  # Главная страница
]