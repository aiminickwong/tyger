from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .models import Proxy


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = Proxy
    # These next two lines tell the view to index lookups by domain
    slug_field = 'domain'
    slug_url_kwarg = 'domain'


class SiteUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported Site in the view code above, remember?
    model = Proxy

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('proxies:detail',
                       kwargs={'domain': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return Proxy.objects.get(domain=self.request.user.username)


class SiteListView(LoginRequiredMixin, ListView):
    model = Proxy
    # These next two lines tell the view to index lookups by username
    slug_field = 'domain'
    slug_url_kwarg = 'domain'
