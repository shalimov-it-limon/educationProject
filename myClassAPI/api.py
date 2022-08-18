import  requests
from settings import base_url


class MyAPIClass:
    def __init__(self):
        self.base_url = base_url

    def get_getToken(self):
        """Получение токена"""
        res = requests.post(base_url+'v1/company/auth/getToken')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
