from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsList.as_view(), name='news-list'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='news-detail'),
    path('tag/<str:tag_name>/', views.news_by_tag, name='news_by_tag'),
]