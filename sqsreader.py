import sys
import time
import boto
import boto3
import boto.sqs
from boto.sqs.message import Message
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sqsspot')
response = table.query(KeyConditionExpression=Key('parameter').eq('queuereadrate'))
items = response['Items']
queuerate = items[0]["value"]

conn = boto.sqs.connect_to_region("us-west-2")

q = conn.get_queue("demosqsspot")

queuedepth = q.count()

while queuedepth >= 0:
    try:
        queuedepth = q.count()
        print(queuedepth)
        if queuedepth == 0:
            print("queue empty")
            time.sleep(5)
        message = q.read(60)
        body = message.get_body()
        print(body)
        timebody, value = body.split(",")
        timestamp = time.ctime(float(timebody))
        print(timestamp)
        print(value)
        q.delete_message(message)
        time.sleep(queuerate)
    except AttributeError:
        print("No message returned")
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
