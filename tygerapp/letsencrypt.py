import subprocess
from allauth.account.decorators import login_required


@login_required
def generate_cert(request, proxy):
    domain = proxy.domain
    email = request.user.email

    generate = subprocess.call(['certbot', 'certonly', '--nginx', '--agree-tos', '--email', email, '-n', '-d', domain])
    print(generate)
    return generate
