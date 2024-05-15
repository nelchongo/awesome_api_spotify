import requests
from .RequestManager import RequestManagerClass
from .AuthorizationManager import AuthorizationManagerClass

class UserManagerClass(RequestManagerClass):
    def __init__(self, auth:AuthorizationManagerClass = None):
        super().__init__(headers = auth.get_request_header())

    def get_me(self) -> requests.Response:
        response = self.get_request('me')
        if response.status_code != 200:
            print("Error: {}\n".format(response.text))
        return response

    def get_top(self, type = 'artist', time_range:str = 'short_term', limit:int = 50) -> requests.Response:
        response = self.get_request('me/top/{}?time_range={}&limit={}'.format(type, time_range, limit))
        if response.status_code != 200:
            print("Error: {}\n".format(response.text))
        return response
            