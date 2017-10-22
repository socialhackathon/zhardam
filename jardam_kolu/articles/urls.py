from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        view=views.ArticleListView.as_view(),
        name='article-list'
    ),
    url(
        r'^p/(?P<pk>\d+)/$',
        view=views.ArticleDetailView.as_view(),
        name='article-detail'
    )
]
