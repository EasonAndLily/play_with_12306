import re
import requests


class Station(object):
    def __init__(self):
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971"
        response = requests.get(url, verify=False)
        self.__station_data = response.text
        data = re.findall(r'([^\u4e00-\u9fa5]+)\|([A-Z]+)', self.__station_data)
        self.__keys = map(lambda key: key[1:], dict(data))
        self.__values = dict(data).values()

    def get_stations_values_keys(self):
        return dict(zip(self.__values, self.__keys))

    def get_stations_keys_values(self):
        return dict(zip(self.__keys, self.__values))
