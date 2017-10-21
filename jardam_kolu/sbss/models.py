from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel, StatusModel
from ordered_model.models import OrderedModel


class Case(TimeStampedModel):
    author = models.ForeignKey(get_user_model(), related_name='cases')
    title = models.CharField()
    description = models.TextField()

    class Meta:
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')


class Solution(TimeStampedModel, OrderedModel):
    case = models.ForeignKey(Case, related_name='solutions')
    text = models.TextField()

    class Meta(OrderedModel.Meta):
        unique_together = ('ordering', 'case')
        verbose_name = _('Solution')
        verbose_name_plural = _('Solutions')


class Complaint(TimeStampedModel, StatusModel):
    INCOMPLETE = 'incomplete'
    VOLUNTEER_REVIEW = 'volunteer review'
    SUCCEED = 'succeed'

    STATUS = (
        (INCOMPLETE, _('incomplete')),
        (VOLUNTEER_REVIEW, _('volunteer review')),
        (SUCCEED, _('succeed')),
    )

    user = models.ForeignKey(get_user_model(), related_name='complaints')
    case = models.ForeignKey(Case)

    class Meta:
        verbose_name = _('Complaint')
        verbose_name_plural = _('Complaints')


class Evidence(TimeStampedModel):
    complaint = models.ForeignKey(Complaint, related_name='evidences')
    solution = models.ForeignKey(Solution, related_name='provided_evidences')
    text = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = _('Evidence')
        verbose_name_plural = _('Evidences')

    def save(self, *args, **kwargs):
        if not self.text and not self.image:
            raise AttributeError("You should provide text or image.")
        return super(Evidence, self).save(*args, **kwargs)
