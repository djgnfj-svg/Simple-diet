#!/bin/bash
sudo supervisorctl start gunicorn
sudo service nginx start