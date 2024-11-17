from django.shortcuts import render, get_object_or_404
from .models import Game
from games.forms import ReviewForm

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    review_form = ReviewForm()
    return render(request, 'games/game_detail.html', {'game': game, 'review_form': review_form})

def add_review(request, catalog_item_id):
    catalog_item = get_object_or_404(CatalogItem, id=catalog_item_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.catalog_item = catalog_item
            review.save()
            catalog_item.calculate_rating()
            return redirect('catalog_detail', id=catalog_item.id)
    else:
        form = ReviewForm()
    return render(request, 'catalog/add_review.html', {'form': form, 'catalog_item': catalog_item})