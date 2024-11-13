from django.contrib import admin
from django.urls import path
from game_web_service import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]
