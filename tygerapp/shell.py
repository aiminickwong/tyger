import subprocess
from allauth.account.decorators import login_required


@login_required
def delete_conf(request, proxy):

    delete = subprocess.call(['rm', '-r', "/etc/nginx/conf.d/" + proxy.domain + ".conf"])
    restart = subprocess.call(['service', 'nginx', 'restart'])
    print(delete)
    print(restart)


@login_required
def restart_nginx(request):
    restart = subprocess.call(['service', 'nginx', 'restart'])
    return restart
