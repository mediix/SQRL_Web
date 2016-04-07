from __future__ import print_function
import boto3
# import os
# import sys
import pyqrcode
import base64

s3_client = boto3.client('s3')

def handler(event, context):
    print('starting')

    # QR code data
    # qrData = base64.urlsafe_b64encode(os.urandom(6))
    qrData = base64.urlsafe_b64encode(event['body']['session_id'])
    print('QR Data = ' + qrData)

    # Create a qr code img
    img = pyqrcode.create(qrData)

    # Save the img to tmp location
    dirPath = '/tmp/'
    fName = qrData + '.svg'
    img.svg(dirPath + fName, scale=6)

    #
    bucket = 'sqrlcontainer'
    key = 'challenges/'

    # Upload file to the bucket
    s3_client.upload_file(dirPath + fName, bucket, key + fName)
