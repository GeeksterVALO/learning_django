from django.urls import path
from .views import IndexView, ArticleView, ArticleCreateView, ArticleCommentsView, article_detail, ArticleFormEditView, ArticleFormDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='article_index'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('tagged/<str:tags>/<int:article_id>/', article_detail, name='article'),
    path('<int:id>/', ArticleView.as_view(), name='article_detail'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view(), name='article_comments'),
]