import json
import sys, os
from base64 import b64encode
from .RequestManager import RequestManagerClass

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from aws.SecretManager import SecretsManagerClass


class AuthorizationManagerClass(RequestManagerClass):
    secret_manager = SecretsManagerClass()

    def __init__(self, secret_token:str = '', secret_credentials:str = ''):
        super().__init__(url = 'https://accounts.spotify.com/api/token')
        #Fetch all the secrets and credentials
        self.secret_token = secret_token
        self.client_token = json.loads(self.secret_manager.get_secret(secret_token))
        self.client_credentials = json.loads(self.secret_manager.get_secret(secret_credentials))
        #Initiallizing credentials
        self.headers =  {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {}'.format(b64encode(f"{self.client_credentials['client_id']}:{self.client_credentials['client_secret']}".encode()).decode())
        }
        #At first run we refresh the token
        self.get_token()

    def get_token(self):
        self.data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.client_token['refresh_token'],
            # 'client_id': self.client_id
        }
        response = self.post_request()
        if response.status_code == 200:
            payload = response.json()
            payload['refresh_token'] = self.client_token['refresh_token']
            self.client_token = payload
            self.secret_manager.update_secret(self.secret_token, json.dumps(payload))
        else:
            self.token = ''
            print("Error: {} {}".format(response, response.text))

    def get_request_header(self) -> dict:
        return {'Authorization': 'Bearer {}'.format(self.client_token['access_token']) }