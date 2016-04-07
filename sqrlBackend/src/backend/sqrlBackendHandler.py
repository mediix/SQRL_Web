import base64
import boto3
import simplejson
import pyqrcode
from backendBaseHandler import backendBaseHandler

class sqrlBackendHandler(backendBaseHandler):
    """
    sqrlBackendHandler API v1.
    sqrlBackendHandler inherits from the backendBaseHandler abstract class.
    inheriting methods needs to be overridden.
    """
    s3_client = boto3.client('s3')

    def __init__(self):
        super(self.__class__, self).__init__()

    def on_generate(self, request_body, request_params):
        """
        :param request_body:
        :param request_params:
        """
        pass

    def on_processing_error(self, event, context, err):
        """
        :param event:
        :param context:
        :param err:
        """
        pass

    def process_request(self, event, context):
        """
        :param event:
        :param context:
        :return:
        """
        try:
            # response = None
            if event['body']['operation'] == "generate":
                self.logger.info("Got into process_request function")
                response = self.build_response(event['body']['session_id'])
            else:
                response = self.on_processing_error(event, context)

        except Exception as err:
            response = self.on_processing_error(event, context, err)
        else:
            print("Successfully Created the response")

        return response

    # -------- Helpers to build the respone type for a request ----------
    def build_response(self, response_type):
        """
        :param path:
        :param response_type:
        :return:
        """
        return simplejson.dumps(
            {
                "result": {
                    "status_code": 0,
                    "response_type": response_type,
                    "qrcode_path": path,
                    "error_message": ''
                }
            },
                sort_keys = True,
                indent = 4
        )

    # Helper functions to generate, record, and save the QRcodes
    def generate_challenge(self, session_id):
        """
        :param session_id:
        :param save_path:
        """
        print("starting to generate QR code")
        self.logger.info("Generating QRCode with %s" % session_id)

        # QR Code data
        qrData = base64.urlsafe_b64encode(session_id)
        print('QR Data: ' + qrData)

        # Create a qr code image
        img = pyqrcode.create(qrData)

        # Save the img in a temorary location
        dirPath = '/tmp/'
        file_name = qrData + '.svg'
        img.svg(dirPath + file_name, scale=6)

        try:
            self.upload_to_s3(dirPath + file_name, file_name)
        except Exception as ex:
            self.logger("Error uploading qrcode: %s" % ex)


    def upload_to_s3(self, path, file_name):
        """
        :param path:
        :param file_name:
        """
        bucket = 'sqrlcontainer'
        key = 'challenges/'

        self.s3_client.upload_file(path, bucket, key + file_name)

    def create_dynamodb_entry(self, session_id, expiration_data):
        """
        :param session_id:
        :param expiration_data:
        """
        pass

