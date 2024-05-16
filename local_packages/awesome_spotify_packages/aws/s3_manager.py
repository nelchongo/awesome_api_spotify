import io
import boto3
import json

class S3Manager():
    def __init__(self, bucket_secret):
        self.client = boto3.client('s3')
        self.bucket_name = bucket_secret.get_secret()

    def put_s3(self, object_key, body):
        self.client.put_object(Bucket = self.bucket_name, Key = object_key, Body = json.dumps(body))