from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=150)
    content = RichTextField(_("Content"))
    on_main_page = models.BooleanField(_("On main page"), default=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=(self.id, ))
