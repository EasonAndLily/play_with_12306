import requests
from .generate_headers import GenerateHeaders
from .cookies import CookieUtils


class API(object):
    def __init__(self, timeout=1000):
        self.__session = requests.session()
        self.__timeout = timeout
        self.__headers = GenerateHeaders.get_headers()
        self.__cookie = CookieUtils()
        expiration_device = GenerateHeaders.get_rail_expiration_device_id()
        self.__cookie.save_cookie(RAIL_EXPIRATION=expiration_device["RAIL_EXPIRATION"],
                                  RAIL_DEVICEID=expiration_device["RAIL_DEVICEID"])

    def get(self, url):
        self.__cookie.load_cookie(self.__session)
        try:
            response = self.__session.get(url, headers=self.__headers, timeout=self.__timeout)
            if response.status_code == 200:
                self.__cookie.save_cookie(**response.cookies.get_dict())
                return response
            else:
                raise BaseException(
                    '请求{0}失败，返回状态码为：{1}'.format(url, response.status_code))
        except Exception as e:
            print(e)

    def post(self, url, data):
        self.__cookie.load_cookie(self.__session)
        try:
            response = self.__session.post(url, data=data, headers=self.__headers, timeout=self.__timeout)
            if response.status_code == 200:
                self.__cookie.save_cookie(**response.cookies.get_dict())
                return response
            else:
                raise BaseException(
                    '请求{0}失败，返回状态码为：{1}'.format(url, response.status_code))
        except Exception as e:
            print(e)


# singleton pattern
api = API()
