from pynamodb.models import Model
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    UTCDateTimeAttribute
)

class Codes(Model):
    """QRCode model class"""
    class Meta:
        table_name = 'qrCodes'
        region = 'us-west-2'
        host = 'https://dynamodb.us-west-2.amazonaws.com'
        # host = 'http://chip:8000'

    class CodeIndex(GlobalSecondaryIndex):
        """"""
        class Meta:
            read_capacity_units = 5
            write_capacity_units = 5
            projection = AllProjection()

        code = UnicodeAttribute(hash_key=True)

    # Required attributes aka database fields
    _id = NumberAttribute(hash_key=True)
    code = UnicodeAttribute(range_key=True)
    s3_bucket_path = UnicodeAttribute(null=False)
    is_expired = NumberAttribute(default=0) # 1 is expired
    date_created = UTCDateTimeAttribute()
    expiration = UTCDateTimeAttribute()
    code_index = CodeIndex()
