import nginx
from allauth.account.decorators import login_required
from django.conf import settings
from tygerapp import letsencrypt
from tygerapp import shell


@login_required
def set_conf(request, proxy):
    config = nginx.Conf()
    server = nginx.Server()
    print(proxy.domain)
    print(proxy.ssl)
    print(proxy.letsencrypt)
    print(proxy.rewriteHTTPS)
    print(proxy.proxypass)

    server.add(
        nginx.Key('listen', '*:80'),
        nginx.Key('server_name', proxy.domain),

    )

    if proxy.rewriteHTTPS:
        server.add(
            nginx.Key('return', '301 https://$server_name$request_uri'),

        )

    if proxy.ssl:
        letsencrypt.generate_cert(request, proxy)
        server.add(
            nginx.Key('listen', '*:443 ssl'),
            nginx.Key('ssl_protocols', 'TLSv1 TLSv1.1 TLSv1.2'),
            nginx.Key('ssl_certificate', '/etc/letsencrypt/live/'+proxy.domain+'/fullchain.pem'),
            nginx.Key('ssl_certificate_key', '/etc/letsencrypt/live/'+proxy.domain+'/privkey.pem'),

        )

    server.add(
        nginx.Location(
            '/',
            nginx.Key('proxy_pass', proxy.proxypass),
            nginx.Key('proxy_set_header', 'Host $host'),
            nginx.Key('proxy_set_header', 'X-Real-IP $remote_addr'),
            nginx.Key('proxy_set_header', 'X-Forwarded-For $proxy_add_x_forwarded_for'),
        )
    )
    config.add(server)
    nginx.dumpf(config, '/etc/nginx/conf.d/' + proxy.domain + '.conf')

    shell.restart_nginx(request)

    return True
