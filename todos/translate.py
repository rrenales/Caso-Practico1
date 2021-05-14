import boto3
import logging
def translate(event, context):
    target_language = event['pathParameters']['target_lang']
    text_id = event['pathParameters']['id']
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    text = table.get_item(
        Key={
            'id': text_id
        }
    )
    
    
    result = client.translate_text(Text=text, SourceLanguageCode="auto",
        TargetLanguageCode=target_language)
    print(result['TranslatedText'])
