from requests.cookies import RequestsCookieJar

from .utils import Utils


class CookieUtils(object):
    @staticmethod
    def save_cookies(cookies):
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        Utils.save_json_data_to_file(cookies, path, "cookies.json")

    @staticmethod
    def load_cookies(session):
        jar = RequestsCookieJar()
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        cookies = Utils.get_json_data_from_file(path, "cookies.json")
        for cookie in cookies:
            jar.set(cookie['name'], cookie['value'])
        session.cookies = jar

    @staticmethod
    def clear_cookies():
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        open(path + "/cookies.json", "w").close()