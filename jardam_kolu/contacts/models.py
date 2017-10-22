from django.contrib.gis.db.models import PointField
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from model_utils.models import TimeStampedModel


class Complex(TimeStampedModel, MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    name = models.CharField(_("Region name"), max_length=255)
    # location = PointField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(_("Contact name"), max_length=255)
    email = models.EmailField(_('Contact email'))
    complex = models.ForeignKey(Complex, null=True, blank=True)
    phone_number = models.CharField(_('Contact phone'), max_length=16, validators=(
        RegexValidator(r'\+?\d+'),
    ))
    address = models.CharField(_('Address'), max_length=255, blank=True, null=True)

    active = models.BooleanField(_('Use in system'), default=True)
    public = models.BooleanField(_('Visibility'), default=True)

    availability = models.CharField(_("Time of availability"), null=True, blank=True, max_length=255)
    additional_phones = models.CharField(_("Phone number"), null=True, blank=True, max_length=255)
    additional_emails = models.CharField(_('Additional emails'), null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.name

    def toggle_active(self):
        self.active = not self.active
        self.save()
        return self.active
