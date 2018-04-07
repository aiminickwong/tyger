from django.shortcuts import render
from django.views.generic import ListView
from tygerapp.proxies.models import Proxy
# Create your views here.


class DashHomeView(ListView):
    model = Proxy
    template_name = 'dashboard/home.html'



