from django.views.generic import DetailView

from . import models


class CaseDetail(DetailView):
    model = models.Case

    def get_queryset(self):
        return self.model.objects.prefetch_related('solutions')


# TODO: create data analysis
