#!/bin/bash
PROJECT_NAME="Simple_diet"
DEPLOY_PATH=/home/ubuntu

PROJECT_PATH=$DEPLOY_PATH/$PROJECT_NAME

# 깃 클론
cd $PROJECT_PATH/

git clone https://github.com/djgnfj-svg/Simple-diet.git

# 시크릿 파일 이동
mv .secrets.json $PROJECT_NAME/backend/.secrets.json


# requirements.txt 설치
pip install -r $PROJECT_NAME/backend/requirements.txt
#static file
python3 $PROJECT_NAME/backend/manage.py collectstatic
#migrate
python3 $PROJECT_NAME/backend/manage.py makemigrations
python3 $PROJECT_NAME/backend/manage.py migrate

# load data
python3 $PROJECT_NAME/backend/manage.py load_data $PROJECT_NAME/backend/_master_data/foods-data.json


# 구니콘 설정 설치
sudo pip3 install gunicorn django
sudo apt-get install supervisor
# 구니콘 설정 이동
cp $PROJECT_NAME/web/gunicorn/django_gunicorn.conf /etc/supervisor/conf.d/django_gunicorn.conf

# npm 설치
cd frontend
sudo apt install -y npm
sudo npm update
sudo npm install -g npm

# node update
sudo curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install nodejs

# npm build
npm i
npm run build


cd ../
# nginx 설치
sudo apt-get install -y nginx
# nginx 설정 이동
cp $PROJECT_NAME/web/nginx/django_nginx.conf /etc/nginx/sites-available/django_nginx.conf
cp $PROJECT_NAME/web/nginx/react_nginx.conf /etc/nginx/sites-available/react_nginx.conf
# nginx 링크
sudo ln /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/
sudo ln /etc/nginx/sites-available/react_nginx.conf /etc/nginx/sites-enabled/

# 구니콘 실행
sudo mkdir /logs
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start gunicorn
# nginx 실행
sudo service nginx start
