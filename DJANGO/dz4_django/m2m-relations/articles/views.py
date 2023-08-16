from django.shortcuts import render
from rest_framework.response import Response
from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().prefetch_related('scope').order_by(ordering)
    context = {'object_list': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)

#new add for cicd

def test_page(request):
    temp = 'hello my frend'
    return render(request, temp)
