# Demo Script for SQS / Spot / Spot Fleet

Baseline instance - ec2-34-221-47-137.us-west-2.compute.amazonaws.com

    ssh -i ~/.ssh/AWSLinuxKeys090418.pem ec2-user@ec2-34-221-47-137.us-west-2.compute.amazonaws.com

## Install required software
    sudo yum install -y gcc python-pip git
    sudo pip install boto3

## Copy deployment assets from GIT repository
    git clone https://github.com/smittoid/sqsspot.git /home/ec2-user/sqsspot

## Set up script to run as a daemon
>Copy startup script to /etc/init.d/sqsreaderservice

    mkdir /opt/sqsspot
    cp /home/ec2-user/sqsspot/sqsreader.py /opt/sqsspot/
    chmod 755 /opt/sqsspot/sqsreader.py
    cp /home/ec2-user/sqsspot/sqsreaderservice /etc/init.d/sqsreaderservice
    chmod 755 /etc/init.d/sqsreaderservice
    /sbin/chkconfig sqsreaderservice on
    service sqsreaderservice start


