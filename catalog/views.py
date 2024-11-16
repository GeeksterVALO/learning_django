from django.shortcuts import render, get_object_or_404
from .models import CatalogItem

def catalog_list(request):
    catalog_items = CatalogItem.objects.all()
    return render(request, 'catalog/catalog_list.html', {'catalog_items': catalog_items})

def catalog_detail(request, id):
    catalog_item = get_object_or_404(CatalogItem, id=id)
    return render(request, 'catalog/catalog_detail.html', {'catalog_item': catalog_item})