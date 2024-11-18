from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_list, name='catalog_list'),
    path('<int:id>/', views.catalog_detail, name='catalog_detail'),
    path('items/', views.CatalogItemList.as_view(), name='catalogitem-list'),
    path('items/<int:pk>/', views.CatalogItemDetail.as_view(), name='catalogitem-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
]