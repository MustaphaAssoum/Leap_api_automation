import requests
from requests import Response


class ApiOperations:
    def __init__(self, base_url: str, endpoint: str):
        self.url = f'{base_url}/{endpoint}'

    def check_endpoint(self):
        return requests.get(self.url)

    def read(self, resource: str, **kwargs) -> Response:
        url = f'{self.url}/{resource}'
        resp = requests.get(url, **kwargs)
        return resp

    def create(self, resource: str, data: str, **kwargs) -> Response:
        url = f'{self.url}/{resource}'
        resp = requests.post(url, data=data, **kwargs)
        return resp

    def update(self, resource: str, data: str, **kwargs) -> Response:
        url = f'{self.url}/{resource}'
        resp = requests.put(url, data=data, **kwargs)
        return resp

    def delete(self, resource: str, **kwargs) -> Response:
        url = f'{self.url}/{resource}'
        resp = requests.delete(url, **kwargs)
        return resp
