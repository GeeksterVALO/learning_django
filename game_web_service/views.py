from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from game_web_service.article.models import Article
from game_web_service.article.forms import ArticleForm

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_index')
        return render(request, 'articles/create.html', {'form': form})

class ArticleCommentsView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
        return render(request, 'articles/comments.html', context={'comment': comment})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={'articles': articles})

def about(request):
    return render(request, 'about.html')

def article_detail(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")