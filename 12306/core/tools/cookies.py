from http import cookiejar

import requests
import urllib3

from .utils import Utils


class CookieUtils(object):
    def __init__(self):
        urllib3.disable_warnings()
        self.__cookie = cookiejar.LWPCookieJar(Utils.get_root_path() + '/config/cookie.txt')

    def save_cookie(self, **kwargs):
        requests.utils.cookiejar_from_dict({k: v for k, v in kwargs.items()}, self.__cookie)
        self.__cookie.save(ignore_discard=True, ignore_expires=True)

    def load_cookie(self, session):
        self.__cookie.load(ignore_discard=True, ignore_expires=True)
        session.cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(self.__cookie))

    def clear_local_cookie(self, session, key=None):
        session.cookies.set(key, None) if key else session.cookies.clear()

    def clear_session_cookie(self):
        self.__cookie.clear()
        self.__cookie.save()
