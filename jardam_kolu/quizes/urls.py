from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(
        r'^scenario/$',
        view=views.get_scenario,
        name='get-scenario'
    ),
    url(
        r'^$',
        view=TemplateView.as_view(template_name='quizes/quiz.html'),
        name='quiz'
    )
]
