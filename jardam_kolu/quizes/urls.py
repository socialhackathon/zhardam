from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^scenario/$',
        view=views.get_scenario,
        name='get-scenario'
    )
]
