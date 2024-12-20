from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('games/', include('games.urls')),
    path('catalog/', include('catalog.urls')),
    path('', views.home, name='home'),  # Главная страница
]