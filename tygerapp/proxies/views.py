from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, TemplateView
from django.contrib import messages
from .models import Proxy
from .forms import ProxyForm, ProxyUpdate, ProxyDelete
from tygerapp.nginx import set_conf
from tygerapp.shell import delete_conf


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = Proxy
    # These next two lines tell the view to index lookups by domain
    slug_field = 'domain'
    slug_url_kwarg = 'domain'


@login_required
def save_site(request):
    if request.method == "POST":
        form = ProxyForm(request.POST)
        if form.is_valid():
            proxy = form.save(commit=False)
            proxy.domain = form.cleaned_data['domain']
            proxy.ssl = form.cleaned_data['ssl']
            proxy.letsencrypt = form.cleaned_data['letsencrypt']
            proxy.rewriteHTTPS = form.cleaned_data['rewriteHTTPS']
            proxy.proxypass = form.cleaned_data['proxypass']

            proxy.save()
            set_conf(request, proxy=proxy)
        messages.success(request, 'Proxy Saved!')
        return redirect('proxies:list')
    else:
        form = ProxyForm()

    return render(request, 'proxies/proxy_form.html', {'form': form})


@login_required
def update_site(request, domain):
    proxy = get_object_or_404(Proxy, domain=domain)
    if request.method == "POST":
        form = ProxyForm(request.POST, instance=proxy)
        if form.is_valid():
            proxy.ssl = form.cleaned_data['ssl']
            proxy.letsencrypt = form.cleaned_data['letsencrypt']
            proxy.rewriteHTTPS = form.cleaned_data['rewriteHTTPS']
            proxy.proxypass = form.cleaned_data['proxypass']
            proxy.save()
            messages.success(request, 'Domain amended successfully!')
            return redirect('proxies:detail', domain=proxy.domain)
    else:
        form = ProxyUpdate(instance=proxy)
    return render(request, 'proxies/proxy_update.html', {'form': form})


@login_required
def delete_site(request, domain):
    proxy = get_object_or_404(Proxy, domain=domain)
    if request.method == "POST":
        delete_conf(request, proxy=proxy)
        proxy.delete()
        messages.success(request, 'Domain deleted successfully!')
        return redirect('proxies:list')
    else:
        return render(request, 'proxies/proxy_delete.html', {'proxy': proxy})


class SiteListView(LoginRequiredMixin, ListView):
    model = Proxy
    # These next two lines tell the view to index lookups by username
    slug_field = 'domain'
    slug_url_kwarg = 'domain'
