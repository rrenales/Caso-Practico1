import os

import boto3
#dynamodb = boto3.resource('dynamodb')
from .todoTableClass import delete_todo

def delete(event, context):
    response =  delete_todo('id')
     
    # create a response
    response = {
        "statusCode": 200
    }

    return response
