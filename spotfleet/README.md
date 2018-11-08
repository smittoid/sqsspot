# Spot Fleet Configuration

Create a Spot Fleet request:

    aws ec2 request-spot-fleet --spot-fleet-request-config file://fleetrequest.json

Configure Spot Fleet request as an Application Auto-scaling target

    aws application-autoscaling register-scalable-target --service-namespace ec2 --resource-id spot-fleet-request/sfr-522565cc-b9fe-4e48-9fc1-6940944c6de9 --scalable-dimension "ec2:spot-fleet-request:TargetCapacity" --role-arn "arn:aws:iam::726467997675:role/aws-service-role/ec2.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest" --min-capacity 0 --max-capacity 10

Configure scaling policies

    aws application-autoscaling put-scaling-policy --cli-input-json file://scalingpolicy-scaleup50.json
    aws application-autoscaling put-scaling-policy --cli-input-json file://scalingpolicy-scaleup10.json
    aws application-autoscaling put-scaling-policy --cli-input-json file://scalingpolicy-scaledown5.json

### Define CloudWatch Alarms for Scaling Policy Triggers

Above 10

    aws cloudwatch put-metric-alarm --alarm-name "SpotSQSAbove10" --metric-name "ApproximateNumberOfMessagesVisible" --dimensions "Name = QueueName, Value = demosqsspot" --period 60 --evaluation-periods 1 --threshold 10 --comparison-operator GreaterThanOrEqualToThreshold --statistic Sum --namespace "AWS/SQS" --alarm-actions arn:aws:autoscaling:us-west-2:726467997675:scalingPolicy:89017300-7df3-474f-b02e-28e237633bdd:resource/ec2/spot-fleet-request/sfr-522565cc-b9fe-4e48-9fc1-6940944c6de9:policyName/ScaleUp10

Above 50

    aws cloudwatch put-metric-alarm --alarm-name "SpotSQSAbove50" --metric-name "ApproximateNumberOfMessagesVisible" --dimensions "Name = QueueName, Value = demosqsspot" --period 30 --evaluation-periods 1 --threshold 50 --comparison-operator GreaterThanOrEqualToThreshold --statistic Sum --namespace "AWS/SQS" --alarm-actions arn:aws:autoscaling:us-west-2:726467997675:scalingPolicy:89017300-7df3-474f-b02e-28e237633bdd:resource/ec2/spot-fleet-request/sfr-522565cc-b9fe-4e48-9fc1-6940944c6de9:policyName/ScaleUp50

Below 5

    aws cloudwatch put-metric-alarm --alarm-name "SpotSQSBelow5" --metric-name "ApproximateNumberOfMessagesVisible" --dimensions "Name = QueueName, Value = demosqsspot" --period 60 --evaluation-periods 1 --threshold 5 --comparison-operator LessThanOrEqualToThreshold --statistic Sum --namespace "AWS/SQS" --alarm-actions arn:aws:autoscaling:us-west-2:726467997675:scalingPolicy:89017300-7df3-474f-b02e-28e237633bdd:resource/ec2/spot-fleet-request/sfr-522565cc-b9fe-4e48-9fc1-6940944c6de9:policyName/ScaleDown5
