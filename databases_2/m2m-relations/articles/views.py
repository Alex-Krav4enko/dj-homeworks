from django.views.generic import ListView
from django.shortcuts import render

from .models import Article
from .models import Relationship


def articles_list(request):
    template = 'articles/news.html'
    # articles_with_deps = Relationship.objects.all()
    articles = Article.objects.all()
    context = {'object_list': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
