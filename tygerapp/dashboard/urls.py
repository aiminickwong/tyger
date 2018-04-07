from django.conf.urls import url
from . import views
app_name = 'dashboard'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.DashHomeView.as_view(),
        name='dashboard'
    ),

]
