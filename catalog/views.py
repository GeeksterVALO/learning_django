from django.shortcuts import render, get_object_or_404
from .models import CatalogItem, Category
from rest_framework import generics
from .serializers import CatalogItemSerializer, CategorySerializer

def catalog_list(request):
    catalog_items = CatalogItem.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        catalog_items = catalog_items.filter(categories__id=selected_category)
    context = {
        'catalog_items': catalog_items,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'catalog/catalog_list.html', context)

def catalog_detail(request, id):
    catalog_item = get_object_or_404(CatalogItem, id=id)
    return render(request, 'catalog/catalog_detail.html', {'catalog_item': catalog_item})

class CatalogItemList(generics.ListCreateAPIView):
    queryset = CatalogItem.objects.all()
    serializer_class = CatalogItemSerializer

class CatalogItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatalogItem.objects.all()
    serializer_class = CatalogItemSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer