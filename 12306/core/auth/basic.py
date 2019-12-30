import requests
from captcha import Captcha
import urllib3

class BasicAuth(object):

    def __init__(self, session, username, password, answer):
        self.__data = {
            "username": username,
            "password": password,
            "appid": "otn",
            "answer": answer
        }
        self.__session = session
        self.__headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100 Safari/537.36',
            "Host": "kyfw.12306.cn",
            "Origin": "https://kyfw.12306.cn",
            "Referer": "https://kyfw.12306.cn/otn/resources/login.html",
        }

    def login(self):
        login_url = "https://kyfw.12306.cn/passport/web/login"
        self.__session.cookies = requests.utils.add_dict_to_cookiejar(self.__session.cookies, {
            "Cookie": "RAIL_DEVICEID=BjIRSVVumHArn35g_X9jrAbQkR9pBaN34uNTTTeD30yzKjPy1Lw66hcxHssEad6Hj3MBSDuywDt6b0A31wvNwY5cYFzuEByjhSPreuHB36CgbIKVqYjSDP"
                      "_kMer8MkXZrWtMJmJf-pbZDGylBUog-e3w2RNJB2es"})

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = self.__session.post(login_url, data=self.__data, headers=self.__headers, verify=False)
        res.encoding = "utf-8"
        data = res.json()
        if data["result_code"] == 0:
            print "Login successfully!"
            return {
                "is_login": True,
                "uamtk": data["uamtk"]
            }
        else:
            print "Login failed!"
            return {
                "is_login": False
            }

    def get_apptk(self):
        url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = self.__session.post(url, data={"appid": "otn"}, headers=self.__headers, verify=False)
        res.encoding = "utf-8"
        print res.text
        data = res.json()
        if data["result_code"] == 0:
            print "Get new apptk successfully!"
            return {
                "get_apptk_successful": True,
                "newapptk": data["newapptk"]
            }
        else:
            print "Get new apptk failed!"
            return {
                "get_apptk_successful": False,
            }


if __name__ == '__main__':
    session = requests.session()
    result = Captcha.run(session)
    if result["is_successful"]:
        aut = BasicAuth(session, "test", "test", result["answer"])
        aut.login()
        aut.get_apptk()
    else:
        print "Please check captcha again!"
