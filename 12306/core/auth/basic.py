import os

import requests
import json


class BasicAuth(object):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__c

    def login(self):
        return requests.post("https://kyfw.12306.cn/passport/web/login", auth=(self.__username, self.__password))

if __name__ == '__main__':
    BasicAuth.get_captcha()
