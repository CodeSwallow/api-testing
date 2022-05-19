import requests


class BaseService:
    BASE_URL = 'https://gorest.co.in/public/v2'
    HEADERS = {
        'Authorization': 'Bearer 09b502827908bd7b2fa5ddb1ebe820dfc511c6a2043b50632bacb79ffc902aa6'
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
