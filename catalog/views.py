from django.shortcuts import render, get_object_or_404
from games.models import Game, Category

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