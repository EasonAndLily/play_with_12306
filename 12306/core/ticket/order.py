# -*- coding: UTF-8 -*-
import sys

sys.path.append('../../core')
from config import config
from tools.api_request import api
from .ticket import Ticket


class Order(object):
    def __init__(self):
        self.__train_date = config.TRAIN_DATA
        self.__from_station_name = config.FROM_STATION
        self.__to_station_name = config.END_STATION
        self.__train_number = config.TRAIN_NUMBER
        self.__submit_url = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"

    def submit_order(self):
        ticket = Ticket()
        secret = ticket.get_train_secret(self.__train_number)
        data = {
            "secretStr": secret,
            "train_date": self.__train_date,
            "back_train_date": self.__train_date,
            "tour_flag": "dc",
            "purpose_codes": "ADULT",
            "query_from_station_name": self.__from_station_name,
            "query_to_station_name": self.__to_station_name,
            "undefined": ""
        }
        res = api.post(self.__submit_url, data=data)
        result = res.json()
        if result["status"] and result['data'] == 'N':
            print("订单提交成功！")
        else:
            print("订单提交失败！系统自动退出...")
            sys.exit(0)

    @staticmethod
    def check_order_info(session, passenger_str, ticket_str, submit_token):
        url = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
        params = {
            "cancel_flag": 2,
            "bed_level_order_num": "000000000000000000000000000000",
            "passengerTicketStr": ticket_str,
            "oldPassengerStr": passenger_str,
            "tour_flag": "dc",
            "randCode": "",
            "whatsSelect": 1,
            "sessionId": "",
            "sig": "",
            "scene": "nc_login",
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": submit_token
        }
        res = session.post(url, data=params)
        result = res.json()
        if result["status"]:
            print("Check order successfully!")
            return result["data"]
        else:
            print("Check Order Failed!")
            return False
