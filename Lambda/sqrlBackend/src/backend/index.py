from __future__ import print_function
import logging
import json
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
    # try:
    #     os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAIQ3I7Q4Y7KP3ZZ4A'
    #     os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
    #     os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
    # except Exception as err:
    #     logger.info("Error updating environment variables.", err)
    # else:
    #     logger.info("Environment variables have been successfully updated.")

    operation = sqrlBackendHandler()
    result = operation.process_request(event, context)

    return json.loads(json.dumps(result))
