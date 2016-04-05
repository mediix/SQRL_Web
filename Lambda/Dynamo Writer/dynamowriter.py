from __future__ import print_function
import boto3
import os
import sys
import base64
import datetime
import time

# Get the service resource
dynamodb = boto3.resource('dynamodb')

def dynamoWriter(event, context):
    #test data
    testdata = base64.urlsafe_b64encode(os.urandom(6))
    now = datetime.datetime.now()
    expiry = now + datetime.timedelta(minutes=10)
    
    table = dynamodb.Table('csci152sqrlchallenges2')
    
    table.put_item(
        Item={
            'qrcode': testdata,
            'creationtime readable': now.strftime("%Y-%m-%d %U:%M:%S"),
            'creationtime': int(round(time.time() * 1000)),
            'expiry readable': expiry.strftime("%Y-%m-%d %U:%M:%S"),
            'expiry': int(round((time.time() + 600) * 1000)),
            'filename': testdata + '.svg',
        }
    )