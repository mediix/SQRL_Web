from __future__ import print_function
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    """
    :param event:
    :param context:
    :return:
    """
    logger.info('Event Received: {}'.format(event))



    return json.loads(json.dumps(result))
