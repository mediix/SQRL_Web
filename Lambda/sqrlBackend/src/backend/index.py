from __future__ import print_function
import os, simplejson as json
import logging
# from model import Codes
from sqrlBackendHandler import sqrlBackendHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    :param event:
    :param context:
    :return:
    """
    logger.info('Event Received: {}'.format(event))

    # Appending AWS credentials to lambda's environment variables
    try:
        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAJR5TLQL4H7YX4ZBQ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
        os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
    except Exception as err:
        logger.info("Error updating environment variables.", err)
        # print("Error updating environment variables.")
    else:
        logger.info("Environment variables have been successfully updated.")

    operation = sqrlBackendHandler()
    result = operation.process_request(event, context)

    # assert isinstance(result, json)
    return result
