from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, FavoriteGameForm
from .models import User
from games.models import Game

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def add_to_favorites(request):
    if request.method == 'POST':
        form = FavoriteGameForm(request.POST)
        if form.is_valid():
            game_id = form.cleaned_data['game_id']
            game = get_object_or_404(Game, id=game_id)
            if game in request.user.favorite_games.all():
                request.user.favorite_games.remove(game)
                messages.success(request, f'{game.title} удалена из избранного.')
            else:
                request.user.favorite_games.add(game)
                messages.success(request, f'{game.title} добавлена в избранное.')
            return redirect('game_detail', id=game.id)
    return redirect('game_list')