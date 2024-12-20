from django.shortcuts import render
from news.models import News

def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    context = {
        'latest_news': latest_news,
    }
    return render(request, 'home.html', context)