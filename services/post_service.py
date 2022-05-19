import requests
from services import base_service


class PostService(base_service.BaseService):

    def __init__(self):
        self.BASE_URL += '/posts'

    def get_comments(self, pk=None, query_params=None):
        url = self.BASE_URL + f'/{pk}/comments'
        if query_params is not None:
            query_list = [f'{key}={query_params[key]}' for key in query_params]
            url += '?' + "&".join(query_list)
        resp = requests.get(url, headers=self.HEADERS)
        response_data = []
        if resp.status_code == 200:
            pass  # Perform Service
        return resp

    def post_comments(self, data, pk=None):
        url = self.BASE_URL + f'/{pk}/comments'
        resp = requests.post(url, data=data, headers=self.HEADERS)
        response_data = []
        if resp.status_code == 201:
            pass  # Perform Service
        return resp
