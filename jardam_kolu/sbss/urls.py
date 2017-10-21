from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<case>\w+)/$',
        view=views.CaseDetail.as_view(),
        name='case-detail'
    ),
]
