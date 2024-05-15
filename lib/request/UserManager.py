from .RequestManager import RequestManagerClass
from .AuthorizationManager import AuthorizationManagerClass

class UserManagerClass(RequestManagerClass):
    def __init__(self, auth:AuthorizationManagerClass = None):
        super().__init__(headers = auth.get_request_header())

    def get_me(self):
        response = super().get_request('me')
        if response.status_code == 200:
            print(response.json())
        else:
            self.me = {}
            print("Error: {}\n".format(response.text))

    def get_top(self, type = 'artists', time_range:str = 'short_term', limit:int = 50):
        response = super().get_request('me/top/{}?time_range={}&limit={}'.format(type, time_range, limit))
        if response.status_code == 200:
            print(response.json())
        else:
            self.me = {}
            print("Error: {}\n".format(response.text))