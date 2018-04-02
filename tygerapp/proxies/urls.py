from django.conf.urls import url

from . import views

app_name = 'proxies'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.SiteListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~update/$',
        view=views.SiteUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.SiteDetailView.as_view(),
        name='detail'
    ),
]
