from django.shortcuts import render, get_object_or_404
from .models import News, Tag
from games.models import Game
from rest_framework import generics
from .serializers import NewsSerializer

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    top_rated_games = Game.objects.order_by('-rating')[:5]
    context = {
        'latest_news': latest_news,
        'top_rated_games': top_rated_games,
    }
    return render(request, 'home.html', context)

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

def news_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    news = tag.news.all()
    return render(request, 'news/news_list.html', {'news': news, 'tag': tag})
