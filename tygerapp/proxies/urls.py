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
        regex=r'^new/$',
        view=views.save_site,
        name='new'
    ),
    url(
        regex=r'^(?P<domain>[\w.@+-]+)/$',
        view=views.SiteDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^edit/(?P<domain>[\w.@+-]+)/$',
        view=views.update_site,
        name='edit'
    ),
    url(
        regex=r'^delete/(?P<domain>[\w.@+-]+)/$',
        view=views.delete_site,
        name='delete'
    ),
]
