import time
import random
import boto
import boto.sqs
from boto.sqs.message import Message

conn = boto.sqs.connect_to_region("us-west-2")

try:
    q = conn.create_queue("demosqsspot")
except:
    q = conn.get_queue("demosqsspot")

val = 20

for i in range(20):
    m = Message()
    t = time.time()
    inc = random.randint(-5, 8)
    #print ("Increment: " + str(inc))
    val = val + inc
    #print("New Value: " + str(val))
    m.set_body(str(t) + ',' + str(val))
    q.write(m)

queuedepth = q.count()

