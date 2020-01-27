# -*- coding: UTF-8 -*-
class Passenger(object):
    def __init__(self, submit_token):
        self.__submit_token = submit_token

    def get_passenger(self, session, names):
        url = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
        data = {
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": self.__submit_token
        }
        res = session.post(url, data=data)
        result = res.json()
        normal_passengers = result["data"]["normal_passengers"]
        passengers = filter(lambda passenger: passenger["passenger_name"] in names, normal_passengers)
        return list(passengers)
