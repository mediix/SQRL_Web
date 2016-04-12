import abc
import logging

from model import Challenge


class backendBaseHandler(object):
    """
    backendBaseHandler base abstract class for handling backend request
    made from sqrl frond-end.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        if not Challenge.exists():
            self.logger.info("Creating table...")
            Challenge.create_table(read_capacity_units=5, write_capacity_units=5, wait=True)

    @abc.abstractmethod
    def on_generate(self, request_body, request_params):
        """
        :param request_body:
        :param request_params:
        """
        pass

    @abc.abstractmethod
    def on_processing_error(self, event, context, err):
        """
        :param event:
        :param context:
        :param err:
        """
        pass