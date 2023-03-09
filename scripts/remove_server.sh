#!/bin/bash
PROJECT_NAME="Simple-diet"
DEPLOY_PATH=/home/ubuntu

PROJECT_PATH=$DEPLOY_PATH/$PROJECT_NAME

# 구니콘 파일 제거
rm -rf /etc/supervisor/conf.d/django_gunicorn.conf
rm -rf /logs

# nginx 파일 제거
rm -rf /etc/nginx/sites-available/django_nginx.conf
rm -rf /etc/nginx/sites-available/react_nginx.conf

# 파일삭제
rm -rf $PROJECT_PATH/Simple_diet

# 서비스 중지
sudo supervisorctl stop gunicorn
sudo service nginx stop


