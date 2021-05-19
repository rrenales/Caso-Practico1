import json
import logging
import os
import time
import uuid
import boto3

#Importamos la funcion put_item
from todoTableClass import put_todo


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    timestamp = str(time.time())
    
    #Hacemos el insert con la funcion put_item
    item = put_todo(data, timestamp)
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
