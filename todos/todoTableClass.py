import boto3
from botocore.exceptions import ClientError
import time
import uuid


class todoTable(object):

    def __init__(self, table, dynamodb=None):
        self.tableName = table
        if not dynamodb:
            # In this case dynamodb is the name of the docker container
            # when all the containers are in the same network.
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://dynamodb:8000') 
        self.dynamodb = dynamodb

    def create_todo_table(self):
        table = self.dynamodb.create_table(
            TableName=self.tableName,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter(
            'table_exists').wait(TableName=self.tableName)
        if (table.table_status != 'ACTIVE'):
            raise AssertionError()

        return table

    def delete_todo_table(self):
        table = self.dynamodb.Table(self.tableName)
        table.delete()

    def put_todo(self,data, timestamp):
        #table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
        item = {
            'id': str(uuid.uuid1()),
            'text': data['text'],
            'checked': False,
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }

         # write the todo to the database
        table.put_item(Item=item)
        return item


    def get_todo(self,id):
        #table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        result = table.get_item(
            Key={
                'id': event['pathParameters']['id']
            }
    )
        return result
    
    def scan_todo(self):
        #table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        # fetch all todos from the database
        scan = table.scan()
        return result
        
    def update_todo(self, text, id, checked):
        timestamp = int(time.time() * 1000)
         # update the todo in the database
        result = table.update_item(
            Key={
                'id': event['pathParameters']['id']
            },
            ExpressionAttributeNames={
              '#todo_text': 'text',
            },
            ExpressionAttributeValues={
              ':text': data['text'],
              ':checked': data['checked'],
              ':updatedAt': timestamp,
            },
            UpdateExpression='SET #todo_text = :text, '
                             'checked = :checked, '
                             'updatedAt = :updatedAt',
            ReturnValues='ALL_NEW',
        )
        return result
        
    def delete_todo(self, id):
        
        # delete the todo from the database
        table.delete_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )

