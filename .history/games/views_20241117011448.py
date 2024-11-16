from django.shortcuts import render, get_object_or_404
from .models import Game
from .forms import ReviewForm

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    review_form = ReviewForm()
    return render(request, 'games/game_detail.html', {'game': game, 'review_form': review_form})

def add_review(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.game = game
            review.save()
            game.calculate_rating()
            return redirect('game_detail', id=game.id)
    else:
        form = ReviewForm()
    return render(request, 'games/add_review.html', {'form': form, 'game': game})