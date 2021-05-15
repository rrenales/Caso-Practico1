import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def translate(event, context):
    client = boto3.client('translate', region_name="us-east-1")
    
    target_language = event['pathParameters']['target_lang']
    text_id = event['pathParameters']['id']
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': text_id
        }
    )
    
    
    resultTranslate = client.translate_text(Text=result['Item']['text'], SourceLanguageCode="auto",
        TargetLanguageCode=target_language)
    
    #return response
    result['Item']['text'] = resultTranslate['TranslatedText']
    
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response