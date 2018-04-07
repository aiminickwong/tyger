# Generated by Django 2.0.3 on 2018-04-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0002_auto_20180402_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxy',
            name='letsencrypt',
            field=models.BooleanField(default=False, verbose_name='LetsEncrypt?'),
        ),
        migrations.AddField(
            model_name='proxy',
            name='proxypass',
            field=models.CharField(blank=True, max_length=255, verbose_name='Proxy Address'),
        ),
        migrations.AddField(
            model_name='proxy',
            name='rewriteHTTPS',
            field=models.BooleanField(default=True, verbose_name='Rewrite to HTTPS?'),
        ),
        migrations.AddField(
            model_name='proxy',
            name='ssl',
            field=models.BooleanField(default=False, verbose_name='SSL?'),
        ),
    ]