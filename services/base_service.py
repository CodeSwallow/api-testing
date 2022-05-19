import requests
from decouple import config


class BaseService:
    BASE_URL = 'https://gorest.co.in/public/v2'
    TOKEN = config('AUTHORIZATION')
    HEADERS = {
        'Authorization': TOKEN
    }

    def get_list(self, query_params=None):
        url = self.BASE_URL
        if query_params is not None:
            query_list = [f'{key}={query_params[key]}' for key in query_params]
            url += '?' + "&".join(query_list)
        resp = requests.get(url, headers=self.HEADERS)
        if resp.status_code == 200:
            pass  # Perform Service
        return resp

    def get_detail(self, pk=None):
        url = self.BASE_URL
        if pk is not None:
            url += f'/{pk}'
        resp = requests.get(url, headers=self.HEADERS)
        print(resp)
        if resp.status_code == 200:
            pass  # Perform Service
        return resp
