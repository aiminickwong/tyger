import subprocess


def delete_conf(proxy):

    subprocess.call(["rm", "-rf", "/etc/nginx/conf.d" + proxy.domain + ".conf"])
