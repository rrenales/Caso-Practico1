import boto3

client = boto3.client('translate', region_name="us-eat-1")
text = "Hola soc el ruben"
result = client.translate_text(Text=text, SourceLanguageCode="auto",
    TargetLanguageCode="en")
print(result['TranslatedText'])