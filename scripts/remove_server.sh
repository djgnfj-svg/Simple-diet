#!/bin/bash

# 3. react build
# 4. 서버 재시작

sudo supervisorctl stop gunicorn
sudo service nginx stop
