from django.shortcuts import render
from django.views.generic import ListView
from tygerapp.proxies.models import Proxy
from allauth.account.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class DashHomeView(LoginRequiredMixin, ListView):
    model = Proxy
    template_name = 'dashboard/home.html'



