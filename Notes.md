# Other scripts used in the process

## Create launch template from CLI
Defines AMI, Instance Type, and Subnet

Amazon Linux 2 Latest AMI - ami-0d1000aff9a9bad89
Instance Type - m4.large
Subnet - subnet-60291138

## Not used - Install "forever" from NPM 
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
sudo yum install -y nodejs
sudo npm install -g forever

## Upload deployment assets to S3
    aws s3 cp ./sqsreaderservice s3://smittyw-e1-demos/sqsspot
    aws s3 cp ./sqsspotinstaller.sh s3://smittyw-e1-demos/sqsspot
    aws s3 cp ./sqsreader.py s3://smittyw-e1-demos/sqsspot

## Copy deployment assets from S3
    aws s3 cp ./sqsreaderservice s3://smittyw-e1-demos/sqsspot
    aws s3 cp ./sqsspotinstaller.sh s3://smittyw-e1-demos/sqsspot
    aws s3 cp ./sqsreader.py s3://smittyw-e1-demos/sqsspot

## Direct copy assets via SCP
    scp -i ~/.ssh/AWSLinuxKeys090418.pem ./sqsreader.py ec2-user@ec2-34-221-47-137.us-west-2.compute.amazonaws.com:/home/ec2-user



