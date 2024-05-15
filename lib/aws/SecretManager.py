import boto3
from botocore.exceptions import ClientError
import json

class SecretsManagerClass:
    def __init__(self):
        self.client = boto3.client(service_name='secretsmanager', region_name='us-east-1')

    def update_secret(self, secret_name:str, secret_value:str):
        try:
            self.client.update_secret(SecretId = secret_name, SecretString = secret_value)
            print(f"Secret '{secret_name}' added successfully.")
        except ClientError as e:
            print("Failed to add secret:", e)

    def get_secret(self, secret_name):
        try:
            response = self.client.get_secret_value(SecretId = secret_name)
            if 'SecretString' in response:
                return response['SecretString']
            else:
                return response['SecretBinary']
        except ClientError as e:
            print("Failed to retrieve secret:", e)