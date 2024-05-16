import boto3
from botocore.exceptions import ClientError

class SecretManager:
    def __init__(self, secret_name:str = ''):
        self.client = boto3.client(service_name='secretsmanager', region_name='us-east-1')
        self.secret_name = secret_name

    def update_secret(self, secret_value:str):
        try:
            self.client.update_secret(SecretId = self.secret_name, SecretString = secret_value)
            print(f"Secret '{self.secret_name}' added successfully.")
        except ClientError as e:
            print("Failed to add secret:", e)

    def get_secret(self):
        try:
            response = self.client.get_secret_value(SecretId = self.secret_name)
            if 'SecretString' in response:
                return response['SecretString']
            else:
                return response['SecretBinary']
        except ClientError as e:
            print("Failed to retrieve secret:", e)