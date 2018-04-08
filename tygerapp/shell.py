import subprocess


def delete_conf(proxy):

    delete = subprocess.call(['rm', '-r', "/etc/nginx/conf.d/" + proxy.domain + ".conf"])
    print(delete)