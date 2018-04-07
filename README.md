# tyger
Nginx Reverse Proxy Manager

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