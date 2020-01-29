import requests
from .generate_headers import GenerateHeaders


class API(object):
    def __init__(self, timeout=1000):
        self.__session = requests.session()
        self.__timeout = timeout
        self.__headers = GenerateHeaders.get_headers()

    def get(self, url):
        try:
            response = self.__session.get(url, headers=self.__headers, timeout=self.__timeout)
            if response.status_code == 200:
                return response
            else:
                raise BaseException(
                    '请求{0}失败，返回状态码为：{1}'.format(url, response.status_code))
        except Exception as e:
            print(e)

    def post(self, url, data):
        try:
            response = self.__session.post(url, data=data, headers=self.__headers, timeout=self.__timeout)
            if response.status_code == 200:
                return response
            else:
                raise BaseException(
                    '请求{0}失败，返回状态码为：{1}'.format(url, response.status_code))
        except Exception as e:
            print(e)
