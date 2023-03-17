#!/bin/bash
PROJECT_NAME="Simple-diet"
PROJECT_BACKEND_NAME="backend"
PROJECT_BACKEND_PATH=$PROJECT_NAME/$PROJECT_BACKEND_NAME

DEPLOY_PATH=/home/ubuntu

PROJECT_PATH=$DEPLOY_PATH/$PROJECT_NAME

# 깃 클론
cd $DEPLOY_PATH/

git clone https://github.com/djgnfj-svg/Simple-diet.git
# 시크릿 파일 이동
cp $DEPLOY_PATH/.secrets.json $PROJECT_BACKEND_PATH/.secrets.json


# requirements.txt 설치
pip install -r $PROJECT_BACKEND_PATH/requirements.txt
#static file
python3 $PROJECT_BACKEND_PATH/manage.py collectstatic
#migrate
python3 $PROJECT_BACKEND_PATH/manage.py makemigrations
python3 $PROJECT_BACKEND_PATH/manage.py migrate

# load data RDS일 경우 조금 거시기해짐...
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_master_data/food-Category.json
python3 $PROJECT_BACKEND_PATH/manage.py loaddata $PROJECT_BACKEND_PATH/_master_data/foods-data.json


# npm 설치
# /home/ubuntu/Simple-diet/frontend
cd $PROJECT_NAME/frontend
# sudo apt install -y npm
# sudo npm update
# sudo npm install -g npm

# node update
sudo curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install nodejs

# npm install
sudo npm i

# npm buffer add
# set NODE_OPTIONS=--max_old_space_size=4096

# sudo dd if=/dev/zero of=/mnt/swapfile bs=1M count=2048
# sudo mkswap /mnt/swapfile
# sudo swapon /mnt/swapfile

# npm build
sudo npm run build


# 구니콘 설정 이동
cd ..
cp web/gunicorn/django_gunicorn.conf /etc/supervisor/conf.d/django_gunicorn.conf

# robots.txt sitemap.xml
cp web/robots.txt /etc/nginx/sites-available/robots.txt
cp web/sitemap.xml /etc/nginx/sites-available/sitemap.xml

# nginx 설치
sudo apt-get install -y nginx
# nginx 설정 이동
cp web/nginx/django_nginx.conf /etc/nginx/sites-available/django_nginx.conf
cp web/nginx/react_nginx.conf /etc/nginx/sites-available/react_nginx.conf
# nginx 링크
sudo ln /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/
sudo ln /etc/nginx/sites-available/react_nginx.conf /etc/nginx/sites-enabled/

# 구니콘 실행
sudo mkdir /logs
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart gunicorn

# nginx 실행
sudo service nginx restart
