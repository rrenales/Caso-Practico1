import os
import json

from todos import decimalencoder
import boto3
#dynamodb = boto3.resource('dynamodb')
from .todoTableClass import get_todo

def get(event, context):

    # Llamamos a todo get_todo para listar en la dynamo db.
    result = get_todo('id')

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
