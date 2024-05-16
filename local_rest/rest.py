import cherrypy
import requests
import random, string, base64, json
import urllib.parse as urlparse

import sys, os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from awesome_spotify_packages.aws import SecretManager as secret_manager

client_credentials = secret_manager(secret_name = 'dev/awesome_api_spotify/client_credentials')
client_token = secret_manager(secret_name = 'dev/awesome_api_spotify/client_token')
credentials = json.loads(client_credentials.get_secret())

class SpotifyAuthRedirect:
    @cherrypy.expose
    def login(self):
        # Define parameters for the Spotify authorization URL
        params = {
            'response_type': 'code',
            'client_id': credentials['client_id'],
            'scope': 'user-top-read user-read-private user-read-email',
            'redirect_uri': 'http://localhost:8080/callback',
            'state': ''.join(random.sample(string.hexdigits, int(16)))
        }

        # Construct the Spotify authorization URL
        auth_url = 'https://accounts.spotify.com/authorize?' + urlparse.urlencode(params)

        # Perform the redirection
        raise cherrypy.HTTPRedirect(auth_url)

    @cherrypy.expose
    def callback(self, code = None, state = None):
        # Handle the callback parameters
        if code and state:
            # Construct the request body for token exchange
            data = {
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': 'http://localhost:8080/callback'
            }
            # Base64 encode client ID and client secret
            auth_header = base64.b64encode(f"{credentials['client_id']}:{credentials['client_secret']}".encode()).decode()
            # Set headers
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': f'Basic {auth_header}'
            }
            # Make a POST request to exchange the code for a token
            response = requests.post('https://accounts.spotify.com/api/token', data = data, headers = headers)
            client_token.update_secret(json.dumps(response.json()))
            return response.json()
        else:
            return "Missing parameters in callback URL"

if __name__ == '__main__':
    # Configure CherryPy server
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080
    })

    # Mount the API
    cherrypy.tree.mount(SpotifyAuthRedirect(), '/')

    # Start the CherryPy server
    cherrypy.engine.start()
    cherrypy.engine.block()
