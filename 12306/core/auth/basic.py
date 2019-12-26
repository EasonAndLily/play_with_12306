import os

import requests
import json


class BasicAuth(object):
    # def __init__(self, username, password):
    #     self.__username = username
    #     self.__password = password

    # def auth(self):
    #     from requests.auth import HTTPBasicAuth
    #     requests.get("")

    @classmethod
    def get_captcha(cls):
        payload = {'login_site': 'E',
                   'module': 'login',
                   'rand': 'sjrand',
                   '1577282618313': '',
                   'callback': 'jQuery19106363285510594114_1577282571162'}
        res = requests.get("https://kyfw.12306.cn/passport/captcha/captcha-image64", params=payload)
        origin_data = res.text
        start = origin_data.find('{')
        end = origin_data.find('}')
        data = json.loads(origin_data[start: end + 1])
        return data['image']

    @classmethod
    def save_captcha(cls, path, file_name):
        import base64
        image_data = base64.b64decode(cls.get_captcha())
        with open(path + file_name, 'wb') as f:
            f.write(image_data)


if __name__ == '__main__':
    BasicAuth.get_captcha()
