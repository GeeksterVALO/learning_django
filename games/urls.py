from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
]