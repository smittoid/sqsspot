* Demo Script for SQS / Spot / Spot Fleet

Baseline instance - ec2-34-221-47-137.us-west-2.compute.amazonaws.com

ssh -i ~/.ssh/AWSLinuxKeys090418.pem ec2-user@ec2-34-221-47-137.us-west-2.compute.amazonaws.com

* Basic software
sudo yum install -y gcc python-pip
sudo pip install boto

* Install "forever" from NPM 
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
sudo yum install -y nodejs
sudo npm install -g forever

* Copy sqsdemoreader.py
scp -i ~/.ssh/AWSLinuxKeys090418.pem ./sqsdemoreader.py ec2-user@ec2-34-221-47-137.us-west-2.compute.amazonaws.com:/home/ec2-user

* Set up script to run as a daemon
Create startup script: touch /etc/init.d/sqsspotautostart.sh
#!/bin/bash
forever start -c /usr/bin/python /opt/sqsspot/sqsdemoreader.py

* Add startup script to boot
sudo chmod +x /etc/init.d/sqsspotautostart.sh
sudo update-rc.d sqsspotautostart.sh defaults
sudo ln -s /etc/init.d/sqsspotautostart.sh /etc/rc3.d/S99sqsspotautostart.sh


* Create launch template from CLI
Defines AMI, Instance Type, and Subnet

Amazon Linux 2 Latest AMI - ami-0d1000aff9a9bad89
Instance Type - m4.large
Subnet - subnet-60291138