import requests

class RequestManagerClass():
    def __init__(self, url:str = None, headers:dict = None, data:dict = {}, params:dict = {}):
        self.url:str = 'https://api.spotify.com/v1/' if url == None else url
        self.headers:dict = headers
        self.data:dict = data
        self.params:dict = params

    def post_request(self) -> requests.Response:
        return requests.post(self.url, headers = self.headers, data = self.data)

    def get_request(self, url:str) -> requests.Response:
        url:str = self.url + url
        return requests.get(url, params = self.params, headers = self.headers, data = self.data)