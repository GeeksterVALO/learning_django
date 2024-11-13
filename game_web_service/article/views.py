from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Articles',
        'message': 'Welcome to the articles page',
    }
    return render(request, 'article/index.html', context=context)