import sys
import urllib3
sys.path.append('../../core')
from tools.generate_headers import GenerateHeaders


class BasicAuth(object):

    def __init__(self, session, username, password, answer):
        self.__data = {
            "username": username,
            "password": password,
            "appid": "otn",
            "answer": answer
        }
        self.__session = session
        self.__headers = GenerateHeaders.get_headers()

    def login(self):
        login_url = "https://kyfw.12306.cn/passport/web/login"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = self.__session.post(login_url, data=self.__data, headers=self.__headers, verify=False)
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

    def get_apptk(self):
        url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = self.__session.post(url, data={"appid": "otn"}, headers=self.__headers, verify=False)
        res.encoding = "utf-8"
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

    def validate_apptk(self, newapptk):
        url = "https://kyfw.12306.cn/otn/uamauthclient"
        data = {'tk': newapptk}
        res = self.__session.post(url, data=data)
        res.encoding = "utf-8"
        result = res.json()
        if result['result_code'] == 0:
            print "Apptk verify successfully!"
            return {
                "verify_successful": True,
                "username": result["username"],
                "apptk": result["apptk"]
            }
        else:
            print "Apptk verify failed!"
            return {"verify_successful": False}
