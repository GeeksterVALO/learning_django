from django.shortcuts import render, get_object_or_404
from games.models import Game, Category
from rest_framework import generics
from games.serializers import GameSerializer, CategorySerializer

def catalog_list(request):
    games = Game.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        games = games.filter(categories__id=selected_category)
    context = {
        'games': games,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'catalog/catalog_list.html', context)

def catalog_detail(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'catalog/catalog_detail.html', {'game': game})

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer