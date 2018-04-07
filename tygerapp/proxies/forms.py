from .models import Proxy
from django.forms import ModelForm
from django import forms


class ProxyForm(ModelForm):
    class Meta:
        model = Proxy
        fields = ['domain', 'ssl', 'letsencrypt', 'rewriteHTTPS', 'proxypass']
        ssl = forms.BooleanField(widget=forms.CheckboxInput())
        letsencrypt = forms.BooleanField(widget=forms.CheckboxInput())
        rewriteHTTPS = forms.BooleanField(widget=forms.CheckboxInput())


class ProxyDelete(ModelForm):
    class Meta:
        model = Proxy
        fields = ['domain']
        domain = forms.CharField(disabled=True)


class ProxyUpdate(ModelForm):
    class Meta:
        model = Proxy
        fields = ['ssl', 'letsencrypt', 'rewriteHTTPS', 'proxypass']
        ssl = forms.BooleanField(widget=forms.CheckboxInput())
        letsencrypt = forms.BooleanField(widget=forms.CheckboxInput())
        rewriteHTTPS = forms.BooleanField(widget=forms.CheckboxInput())