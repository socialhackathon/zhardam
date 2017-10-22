from django.conf import settings # import the settings file

from jardam_kolu.articles.models import Article


def main_page_articles(request):
    articles = Article.objects.filter(
        on_main_page=True
    )[:3]
    return {
        'main_articles': articles
    }


def disqus_short_name(request):
    return {
        'DISQUS_SHORT_NAME': settings.DISQUS_SHORT_NAME
    }
