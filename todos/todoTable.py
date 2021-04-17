import boto3
from botocore.exceptions import ClientError
import time
import uuid


class todoTable(object):

    def __init__(self, table, dynamodb=None):
        self.tableName = table
        if not dynamodb:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://localhost:8000')
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

    def put_todo(self, text, id=None):
"""  A completar por el alumno. Pista: todos/ToDoPutItem.py """

    def get_todo(self, id):
"""  A completar por el alumno. Pista: todos/ToDoGetItem.py """

    def scan_todo(self):
"""  A completar por el alumno. Pista: todos/ToDoListItems.py """

    def update_todo(self, text, id, checked):
"""  A completar por el alumno. Pista: todos/ToDoUpdateItem.py """

    def delete_todo(self, id):
"""  A completar por el alumno. Pista: todos/ToDoDeleteItem.py """
