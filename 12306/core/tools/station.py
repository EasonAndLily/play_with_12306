# -*- coding: UTF-8 -*-
import os
import re

from .utils import Utils
from .api_request import api


class Station(object):
    def __init__(self):
        if os.path.exists(Utils.get_root_path() + "/config/stations.json"):
            self.__stations = Utils.get_json_data_from_file(Utils.get_root_path() + "/config", "stations.json")
        else:
            self.__stations = Station.request_stations()
            Station.save_stations_to_file(self.__stations)

    def get_stations_value_by_key(self, key):
        return dict(map(reversed, self.__stations.items()))[key]

    def get_station_key_by_values(self, value):
        return self.__stations[value]

    @classmethod
    def request_stations(cls):
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971"
        response = api.get(url)
        data = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
        return dict(data)

    @classmethod
    def save_stations_to_file(cls, stations):
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        Utils.save_json_data_to_file(stations, path, "stations.json")
