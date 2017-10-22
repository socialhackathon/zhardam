from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Administrative(TimeStampedModel):
    name = models.CharField(_("Region name"))


class Contact(TimeStampedModel):
    name = models.CharField(_("Contact name"), max_length=255)

    address = models.CharField(_('Address'), max_length=255, blank=True, null=True)
    regions = models.ManyToManyField(Region,)


    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
