from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article
    queryset = Article.objects.all()
