import sys

from config import config
from src.core.tools.api_request import api


class BasicAuth(object):
    def __init__(self, answer):
        self.__username = config.USERNAME
        self.__password = config.PASSWORD
        self.__answer = answer
        self.__login_url = "https://kyfw.12306.cn/passport/web/login"
        self.__get_apptk_url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
        self.__validate_apptk_url = "https://kyfw.12306.cn/otn/uamauthclient"

    def login(self):
        data = {
            "username": self.__username,
            "password": self.__password,
            "appid": "otn",
            "answer": self.__answer
        }
        response = api.post(self.__login_url, data=data)
        data = response.json()
        if data["result_code"] == 0:
            print("用户" + config.USERNAME + "登陆成功!")
            return data["uamtk"]
        else:
            print("用户" + config.USERNAME + "登陆失败！系统自动退出...")
            sys.exit(0)

    def get_apptk(self):
        res = api.post(self.__get_apptk_url, data={"appid": "otn"})
        data = res.json()
        if data["result_code"] == 0:
            print("获取apptk成功！")
            return data["newapptk"]
        else:
            print("获取apptk失败！系统自动退出...")
            sys.exit(0)

    def validate_apptk(self, newapptk):
        data = {'tk': newapptk}
        res = api.post(self.__validate_apptk_url, data=data)
        result = res.json()
        if result['result_code'] == 0:
            print("apptk认证成功！")
            return result["apptk"]
        else:
            print("apptk认证失败！系统自动退出....")
            sys.exit(0)
