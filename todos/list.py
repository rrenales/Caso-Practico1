import json
import os

from todos import decimalencoder
import boto3
from .todoTableClass import scan_todo


def list(event, context):
    result = scan_todo()
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
