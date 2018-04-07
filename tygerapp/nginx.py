import nginx
from django.conf import settings


def set_conf(proxy):
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
        server.add(
            nginx.Key('listen', '*:443 ssl'),
            nginx.Key('ssl_protocols', 'TLSv1 TLSv1.1 TLSv1.2'),
            nginx.Key('server_name', proxy.domain),
        )

    server.add(
        nginx.Location(
            '/',
            nginx.Key('proxy_pass', proxy.proxypass),
            nginx.Key('proxy_set_header', 'Host $host'),
            nginx.Key('proxy_set_header', 'X - Real - IP $remote_addr'),
            nginx.Key('X - Forwarded - For', '$proxy_add_x_forwarded_for'),
        )
    )
    config.add(server)
    nginx.dumpf(config, '/etc/nginx/Sites-Enabled/' + proxy.domain + '.conf')
