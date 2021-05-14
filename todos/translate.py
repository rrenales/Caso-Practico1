import boto3
import logging
def translate(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    client = boto3.client('translate', region_name="us-eat-1")
    target_language = data['language']
    if target_language == None:
        logging.error("target language data missing")
        raise Exception("Couldn't read the target language")
    text = "Hola soc el ruben"
    result = client.translate_text(Text=text, SourceLanguageCode="auto",
        TargetLanguageCode="en")
    print(result['TranslatedText'])
