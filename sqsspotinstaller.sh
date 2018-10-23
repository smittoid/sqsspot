#!/bin/bash

yum update -y
yum install -y gcc python-pip git
pip install boto

git clone https://github.com/smittoid/sqsspot.git /home/ec2-user/sqsspot

mkdir /opt/sqsspot
cp /home/ec2-user/sqsspot/sqsreader.py /opt/sqsspot/
chmod 755 /opt/sqsspot/sqsreader.py
cp /home/ec2-user/sqsspot/sqsreaderservice /etc/init.d/sqsreaderservice
chmod 755 /etc/init.d/sqsreaderservice
/sbin/chkconfig sqsreaderservice on
service sqsreaderservice start