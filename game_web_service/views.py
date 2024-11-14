from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import Article

class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = {'articles': articles}
        return render(request, 'article/index.html', context)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))

def about(request):
    return render(request, 'about.html')

def article_detail(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")