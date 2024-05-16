import requests
from .request_manager import RequestManager
from .authorization_manager import AuthorizationManager

class UserManager(RequestManager):
    def __init__(self, auth:AuthorizationManager = None):
        super().__init__(headers = auth.get_request_header())

    def get_me(self) -> requests.Response:
        response = self.get_request('me')
        if response.status_code != 200:
            print("Error: {}\n".format(response.text))
        return response

    def get_top(self, type:str = 'artist', time_range:str = 'long_term', offset:int = 0, limit:int = 50) -> requests.Response:
        response = self.get_request('me/top/{}?time_range={}&offset={}&limit={}'.format(type, time_range, offset, limit))
        if response.status_code != 200:
            print("Error: {}\n".format(response.text))
        return response
            