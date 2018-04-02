from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Proxy(models.Model):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    domain = models.CharField(_('Domain Name'), blank=True, max_length=255)

    def __str__(self):
        return self.domain

    def get_absolute_url(self):
        return reverse('proxies:detail', kwargs={'domain': self.domain})
