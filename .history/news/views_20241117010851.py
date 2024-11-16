from django.shortcuts import render, get_object_or_404
from news.models import News

def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    context = {
        'latest_news': latest_news,
    }
    return render(request, 'home.html', context)

def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})