#!/bin/bash
# 현재 문제는 서버가 여러개가 되었을떄 시크릿키가 바뀐다면 어떡해 할 것인가?

# .secrets.json 이동  todo: 이파일을 자동화 해야한다.
# 파일이 외부로 노출되서는 안되는 문제를 해결하지 못했다.
DEPLOY_PATH=/home/ubuntu
mv $DEPLOY_PATH/Simple_Diet/backend/.secrets.json .

# 파일삭제
rm -rf $DEPLOY_PATH/Simple_diet

# 서비스 중지
sudo supervisorctl stop gunicorn
sudo service nginx stop

# 구니콘 파일 제거
rm -rf /etc/supervisor/conf.d/django.conf
rm -rf /logs

# nginx 파일 제거
rm -rf /etc/nginx/sites-available/django.conf
rm -rf /etc/nginx/sites-available/react.conf

