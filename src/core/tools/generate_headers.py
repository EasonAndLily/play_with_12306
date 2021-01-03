import time
from selenium import webdriver
from src.core.tools.utils import Utils


class GenerateHeaders(object):
    @classmethod
    def get_headers(cls):
        return {
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
            "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            "sec-ch-ua-mobile": "?0"
        }

    @classmethod
    def generate_rail_device(cls):
        options = webdriver.ChromeOptions()
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36')
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        driver = webdriver.Chrome()
        driver.get("https://www.12306.cn/index/index.html")
        print("Please wait about 10s.....")
        time.sleep(10)
        rail_device = {
            "device": None,
            "expiration": None
        }
        for cookie in driver.get_cookies():
            if cookie.get("name") == "RAIL_DEVICEID":
                rail_device["device"] = cookie.get("value")
            if cookie.get("name") == "RAIL_EXPIRATION":
                rail_device["expiration"] = cookie.get("value")
        print(rail_device)
        cls.save_device(rail_device)
        print("Generate rail device successfully and save it to device,json file!")
        driver.quit()

    @classmethod
    def save_device(cls, rail_device):
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        Utils.save_json_data_to_file(rail_device, path, "device.json")

    @classmethod
    def get_device(cls):
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        device = Utils.get_json_data_from_file(path, "device.json")
        return {
            "RAIL_EXPIRATION": device["expiration"],
            "RAIL_DEVICEID": device["device"]
        }


if __name__ == '__main__':
    device = GenerateHeaders.get_device()
    print(device)
