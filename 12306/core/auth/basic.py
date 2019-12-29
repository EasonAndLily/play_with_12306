import requests
from captcha import Captcha


class BasicAuth(object):

    def __init__(self, session, username, password, answer):
        self.__data = {
            "username": username,
            "password": password,
            "appid": "otn",
            "answer": answer
        }
        self.__session = session

    def login(self):
        login_url = "https://kyfw.12306.cn/passport/web/login"

        headers = {
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
        self.__session.cookies = requests.utils.add_dict_to_cookiejar(self.__session.cookies, {
            "Cookie": "RAIL_DEVICEID=oU2_ihlKzRnCkvWwbVuHYK-8dD3bt0xCGWXO-zjB1CCJma1ayJNA2VGL8pYedPYXm-0bUi-lLABuMcuv"
                      "_Iy2oYdaAHT5wX5HP0qs4hNfTfzAYF3qRmCGZ9Z9yBQJdIQP08pD9K0v3GTyZHv7GnecUkxXBxqreSQz"})

        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = self.__session.post(login_url, data=self.__data, headers=headers, verify=False)
        res.encoding = "utf-8"
        print res.text
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


if __name__ == '__main__':
    session = requests.session()
    result = Captcha.run(session)
    if result["is_successful"]:
        aut = BasicAuth(session, "test", "test", result["answer"])
        aut.login()
    else:
        print "Please check captcha again!"
