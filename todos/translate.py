import boto3
import logging
def translate(event, context):
    client = boto3.client('translate', region_name="us-east-1")
    
    target_language = event['pathParameters']['target_lang']
    text_id = event['pathParameters']['id']
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    text = table.get_item(
        Key={
            'id': text_id
        }
    )
    
    
    resultTranslate = client.translate_text(Text=result['Item']['text'], SourceLanguageCode="auto",
        TargetLanguageCode=target_language)
    print(resultTranslate['Translatedtext'])
    
    return response
    