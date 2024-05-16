import json
from base64 import b64encode
from .request_manager import RequestManager

class AuthorizationManager(RequestManager):
    def __init__(self, client_token, client_credencial):
        self.url = 'https://accounts.spotify.com/api/token'
        #Fetch all the secrets and credentials
        self.secret_token = json.loads(client_token.get_secret())
        self.secret_credencial = json.loads(client_credencial.get_secret())
        #Initiallizing credentials
        self.headers =  {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {}'.format(b64encode(f"{self.secret_credencial['client_id']}:{self.secret_credencial['client_secret']}".encode()).decode())
        }
        self.data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.secret_token['refresh_token']
        }
        #At first we refresh the token
        self.get_token()

    def get_token(self):
        response = self.post_request()
        if response.status_code == 200:
            payload = response.json()
            payload['refresh_token'] = self.secret_token['refresh_token']
            self.secret_token = payload
        else:
            self.token = ''
            print("Error: {} {}".format(response, response.text))

    def get_request_header(self) -> dict:
        return {'Authorization': 'Bearer {}'.format(self.secret_token['access_token']) }