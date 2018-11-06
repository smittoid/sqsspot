import time
import random
import boto3

sqs = boto3.resource('sqs')

try:
    q = sqs.get_queue_by_name(QueueName="demosqsspot")
except:
    q = sqs.create_queue(QueueName="demosqsspot")

val = 20

for i in range(20):
    t = time.time()
    inc = random.randint(-5, 8)
    #print ("Increment: " + str(inc))
    val = val + inc
    #print("New Value: " + str(val))
    message = (str(t) + ',' + str(val))
    q.send_message(MessageBody=message)

