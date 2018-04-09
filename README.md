# Tyger
Nginx Reverse Proxy Manager aimed at the HomeServer community. 

## Ubuntu Install

Starting with a clean Ubuntu 16.04 Server install. All commands below should be run with **sudo**  or **root** privileges.

    apt-get update && apt-get upgrade -y

Reboot the server. 

Make the app directories ready:

    mkdir /app
    mkdir /app/env

Install the required OS packages:

    apt-get install -y nginx wget nano build-essential python-dev
    
Install the virtual environment for Python and Django:

    pip install virtualenv uwsgi
    
Setup our new python virtualenv:

    virtualenv /app/env/tygerapp
    
Activate it:

    source /app/env/tygerapp/bin/activate
    
Clone the repo to the correct location:

    cd /app
    git clone https://github.com/morph1904/tyger.git tygerapp
    
                
    

### CentOS7 Install (Very rough notes)

sudo yum update -y

rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install -y nginx

sudo firewall-cmd --permanent --zone=public --add-service=http 
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload

#disable SELinux
nano /etc/sysconfig/selinux


yum install -y git nano wget

yum -y install yum-utils

sudo yum -y groupinstall development

sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum -y install python36u python36u-devel python36u-pip certbot

pip3.6 install virtualenv

mkdir /app
mkdir /app/env

git clone https://github.com/morph1904/tyger.git tygerapp

virtualenv /app/env/tyger

source /app/env/tyger/bin/activate

cd /app/tygerapp

pip3.6 install requirements/local.txt

