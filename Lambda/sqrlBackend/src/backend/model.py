from pynamodb.models import Model
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute
)


class Challenge(Model):
    """QRCode model class"""
    class Meta:
        table_name = 'qrCodes'
        region = 'us-west-2'
        host = 'https://dynamodb.us-west-2.amazonaws.com'
        #host = "http://localhost:8000"

    class CodeIndex(GlobalSecondaryIndex):
        """"""
        class Meta:
            read_capacity_units = 5
            write_capacity_units = 5
            projection = AllProjection()
        #
        qrcode = UnicodeAttribute(hash_key=True)

    # Required attributes aka database fields
    qrcode = UnicodeAttribute(hash_key=True)
    readable_date_created = UnicodeAttribute(null=False)
    date_created = NumberAttribute(null=False)
    readable_expiry = UnicodeAttribute(null=False)
    expiry = NumberAttribute(null=False)
    s3_file_path = UnicodeAttribute(null=False)
    is_expired = NumberAttribute(default=0)  # 1 is expired
    user_logged_in = UnicodeAttribute(null=True)
    qrcode_index = CodeIndex()
