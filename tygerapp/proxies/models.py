from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Proxy(models.Model):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    domain = models.CharField(_('Domain Name'), blank=False, max_length=255, unique=True)
    ssl = models.BooleanField(_('SSL?'), default=False,)
    letsencrypt = models.BooleanField(_('LetsEncrypt?'), default=False)
    rewriteHTTPS = models.BooleanField(_('Rewrite to HTTPS?'), default=True)
    proxypass = models.CharField(_('Proxy Address'), blank=True, max_length=255)

    def __str__(self):
        return self.domain

    def get_absolute_url(self):
        return reverse('proxies:detail', kwargs={'domain': self.domain})

