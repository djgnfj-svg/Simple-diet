#!/bin/bash
PROJECT_NAME="Simple-diet"
DEPLOY_PATH=/home/ubuntu

PROJECT_PATH=$DEPLOY_PATH/$PROJECT_NAME

# 구니콘 파일
GUNICORN_FILE="/etc/supervisor/conf.d/django_gunicorn.conf"
# nginx 파일
NGINX_DJANGO_FILE="/etc/nginx/sites-available/django_nginx.conf"
NGINX_REACT_FILE="/etc/nginx/sites-available/react_nginx.conf"

NGINX_DJANGO_FILE_ENABLE="/etc/nginx/sites-enabled/django_nginx.conf"
NGINX_REACT_FILE_ENABLE="/etc/nginx/sites-enabled/react_nginx.conf"
SERVICE_GUNICONR=$(pgrep gunicorn)
SERVICE_NIGNX=$(pgrep nginx)

# 구니콘 파일 제거
if [ -e $GUNICORN_FILE ]; then
    rm -rf $GUNICORN_FILE
    rm -rf /logs
fi

# nginx 파일 제거
if [ -e $NGINX_DJANGO_FILE ]; then
    rm -rf $NGINX_DJANGO_FILE
fi
if [ -e $NGINX_REACT_FILE ] ; then
    rm -rf $NGINX_REACT_FILE
fi

if [ -e $NGINX_DJANGO_FILE_ENABLE ]; then
    rm -rf $NGINX_DJANGO_FILE_ENABLE
fi
if [ -e $NGINX_REACT_FILE_ENABLE ] ; then
    rm -rf $NGINX_REACT_FILE_ENABLE
fi

# 프로젝트 파일삭제
if [ -e $PROJECT_PATH ]; then
    sudo rm -rf $PROJECT_PATH
fi

# 서비스 중지
if [ -z "$SERVICE_GUNICONR" ]; then
    sudo supervisorctl stop gunicorn
fi

if [ -z "$SERVICE_NIGNX" ]; then
    sudo service nginx stop
fi

# nginx + gunicorn 설정파일 삭제
