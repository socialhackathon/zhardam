from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        view=views.ContactsListView.as_view(),
        name='contact-list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        view=views.ContactsDetailView.as_view(),
        name='contact-detail'
    ),
    url(
        r'^(?P<pk>\d+)/show.json$',
        view=views.ContactContactsAPIView.as_view(),
        name='contact-contacts'
    ),
    url(
        r'^(?P<pk>\d+)/show/$',
        view=views.ContactsShowView.as_view(),
        name='contact-show',
    )
]
