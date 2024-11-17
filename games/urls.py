from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.game_detail, name='game_detail'),
    path('<int:game_id>/add_review/', views.add_review, name='add_review'),
]