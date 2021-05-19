import json
import time
import logging
import os

from todos import decimalencoder
import boto3
#dynamodb = boto3.resource('dynamodb')
from .todoTableClass import update_todo

def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return
    
    result = update_todo('text', 'id', 'checked')
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
