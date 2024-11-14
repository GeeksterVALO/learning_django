from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from game_web_service.article.models import Article

# class ArticleIndexView(View):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         context = {'articles': articles}
#         return render(request, 'articles/index.html', context)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

def article_detail(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")