# -*- coding: UTF-8 -*-
import sys

sys.path.append('../../core')
from tools.api_request import api
from config import config


class Passenger(object):
    @classmethod
    def get_passenger(cls, sumbit_token):
        url = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
        data = {
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": sumbit_token
        }
        res = api.post(url, data=data)
        result = res.json()
        normal_passengers = result["data"]["normal_passengers"]
        passengers = filter(lambda passenger: passenger["passenger_name"] in config.PASSENGERS, normal_passengers)
        return list(passengers)
