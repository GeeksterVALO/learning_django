from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:id>/', views.news_detail, name='news_detail'),
    path('tag/<str:tag_name>/', views.news_by_tag, name='news_by_tag'),
]