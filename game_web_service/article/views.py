from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {'articles': articles}
        return render(request, 'article/index.html', context)