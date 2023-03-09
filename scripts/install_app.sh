# pip 등 설치(codedeploy도)
sudo yum update -y
sudo yum install git -y
sudo yum install python3-pip python3-devel python3-setuptools -y

sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install python3
sudo apt-get install -y python3-pip

# Codedeploy 설치 + 실행
sudo yum install -y ruby
sudo yum install wget
wget https://aws-codedeploy-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent start

# 구니콘 설정 설치
sudo pip3 install gunicorn django
sudo apt-get install supervisor