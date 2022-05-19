import requests
from services import base_service


class UserService(base_service.BaseService):
    """
        Service to make API calls to /users endpoint.
        Added functionality could be added on successful response
    """

    def __init__(self):
        self.BASE_URL += '/users'

    def post(self, data):
        url = self.BASE_URL
        resp = requests.post(url, data=data, headers=self.HEADERS)
        if resp.status_code == 201:
            pass  # Perform Service
        return resp

    def put(self, data, pk=None):
        url = self.BASE_URL + f'/{pk}'
        resp = requests.put(url, data=data, headers=self.HEADERS)
        if resp.status_code == 200:
            pass  # Perform Service
        return resp

    def patch(self, data, pk=None):
        url = self.BASE_URL + f'/{pk}'
        resp = requests.patch(url, data=data, headers=self.HEADERS)
        if resp.status_code == 200:
            pass  # Perform Service
        return resp

    def delete(self, pk=None):
        url = self.BASE_URL + f'/{pk}'
        resp = requests.delete(url, headers=self.HEADERS)
        if resp.status_code == 204:
            pass  # Perform Service
        return resp

    def get_posts(self, pk=None, query_params=None):
        url = self.BASE_URL + f'/{pk}/posts'
        if query_params is not None:
            query_list = [f'{key}={query_params[key]}' for key in query_params]
            url += '?' + "&".join(query_list)
        resp = requests.get(url, headers=self.HEADERS)
        if resp.status_code == 200:
            pass  # Perform Service
        return resp

    def post_posts(self, data, pk=None):
        url = self.BASE_URL + f'/{pk}/posts'
        resp = requests.post(url, data=data, headers=self.HEADERS)
        if resp.status_code == 201:
            pass  # Perform Service
        return resp

    def get_todos(self, pk=None, query_params=None):
        url = self.BASE_URL + f'/{pk}/todos'
        if query_params is not None:
            query_list = [f'{key}={query_params[key]}' for key in query_params]
            url += '?' + "&".join(query_list)
        resp = requests.get(url, headers=self.HEADERS)
        if resp.status_code == 200:
            pass  # Perform Service
        return resp

    def post_todos(self, data, pk=None):
        url = self.BASE_URL + f'/{pk}/todos'
        resp = requests.post(url, data=data, headers=self.HEADERS)
        if resp.status_code == 201:
            pass  # Perform Service
        return resp
