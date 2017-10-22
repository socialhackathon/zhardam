from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ArticlesAppConfig(AppConfig):
    name = 'jardam_kolu.articles'
    verbose_name = _('Article management')
