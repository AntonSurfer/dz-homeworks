from django.shortcuts import render
from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related(
        'article_scopes__tag'
    ).order_by('-published_at')
    context = {
        'object_list': articles,
    }
    return render(request, template, context)
