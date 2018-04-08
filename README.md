# tyger
Nginx Reverse Proxy Manager

#CentOS7 Install

sudo yum update -y

rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install -y nginx

sudo firewall-cmd --permanent --zone=public --add-service=http 
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload


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






#Basic install script

sudo add-apt-repository ppa:jonathonf/python-3.6

sudo apt-get update

sudo apt-get install python3.6



mkdir /app
cd /app
git clone https://github.com/morph1904/tyger.git tyger

cd tyger

apt install -y python-pip

pip3 install virtualenv

virtualenv /app/env/tyger

source /app/env/tyger/bin/activate 

pip3 install -r requirements/base.txt

python3 ma