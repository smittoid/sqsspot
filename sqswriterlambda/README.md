# Simple Lambda SQS message generator

Create lambda function and upload Python package: 

    aws lambda create-function --function-name HelloPython --zip-file fileb://sqswriterlambda.zip --role arn:aws:iam::726467997675:role/LambdaSQSFullAccess --handler sqswriterlambda.my_handler --runtime python2.7 --timeout 15 --memory-size 512

Update lambda function code:

    aws lambda update-function-code --function-name sqswriterlambda --zip-file fileb://sqswriterlambda.zip

