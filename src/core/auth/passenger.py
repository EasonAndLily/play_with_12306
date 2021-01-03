# -*- coding: UTF-8 -*-
from src.core.tools.api_request import API
from config import config


class Passenger(object):
    def __init__(self, submit_token):
        self.__get_passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
        self.__submit_token = submit_token
        self.api = API()
        self.__passengers = self.get_passenger()

    def get_passenger(self):
        data = {
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": self.__submit_token
        }
        res = self.api.post(self.__get_passenger_url, data=data)
        result = res.json()
        normal_passengers = result["data"]["normal_passengers"]
        if normal_passengers is not None:
            passengers = filter(lambda passenger: passenger["passenger_name"] in config.PASSENGERS, normal_passengers)
            return list(passengers)
        else:
            raise Exception(result["data"]["exMsg"])

    def get_passengers_str(self):
        passengers = []
        for passenger in self.__passengers:
            passenger_attrs = ["O",
                               passenger['passenger_flag'],
                               passenger['passenger_type'],
                               passenger['passenger_name'],
                               passenger['passenger_id_type_code'],
                               passenger['passenger_id_no'],
                               passenger['mobile_no'],
                               "N",
                               passenger['allEncStr']]
            passengers.append(str.join(",", passenger_attrs))
        return str.join("_", passengers)

    def get_ticket_str(self):
        ticket_str = []
        for passenger in self.__passengers:
            passenger_attrs = [passenger["passenger_name"],
                               passenger['passenger_id_type_code'],
                               passenger['passenger_id_no'],
                               "1"]
            ticket_str.append(str.join(",", passenger_attrs))
        return str.join("_", ticket_str) + "_"
