from requests.cookies import RequestsCookieJar

from .utils import Utils


class CookieUtils(object):
    cookie_file_path = Utils.get_root_path() + "/config"
    cookie_file_name = "cookies.json"

    @classmethod
    def save_cookies(cls, cookies):
        Utils.save_json_data_to_file(cookies, cls.cookie_file_path, cls.cookie_file_name)

    @classmethod
    def load_cookies(cls, session):
        jar = RequestsCookieJar()
        cookies = Utils.get_json_data_from_file(cls.cookie_file_path, cls.cookie_file_name)
        for cookie in cookies:
            jar.set(cookie['name'], cookie['value'])
        session.cookies = jar

    @classmethod
    def clear_cookies(cls):
        open(cls.cookie_file_path + "/" + cls.cookie_file_name, "w").close()

    @classmethod
    def check_cookies(cls):
        cookies_keys = {"uKey", "tk", "JSESSIONID", "RAIL_EXPIRATION", "RAIL_DEVICEID",
                           "route", "BIGipServerotn", "BIGipServerpassport"}
        cookies = Utils.get_json_data_from_file(cls.cookie_file_path, cls.cookie_file_name)
        all_keys = set((cookie['name'] for cookie in cookies))
        missing_cookies = cookies_keys.difference(all_keys)
        if len(missing_cookies) > 0:
            raise Exception("Cookies文件生成失败，缺少如下Cookies：" + ','.join(missing_cookies))
