from django.shortcuts import render, get_object_or_404
from .models import News, Tag

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