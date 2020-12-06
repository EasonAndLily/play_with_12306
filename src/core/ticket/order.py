# -*- coding: UTF-8 -*-
import sys
import time

from src.core.tools.api_request import api
from .ticket import Ticket


class Order(object):
    def __init__(self, config):
        self.__train_date = config.TRAIN_DATA
        self.__from_station_name = config.FROM_STATION
        self.__to_station_name = config.END_STATION
        self.__train_number = config.TRAIN_NUMBER
        self.__submit_url = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
        self.__check_order_info = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
        self.__get_order_info_url = "https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime"
        self.__check_order_for_queue = "https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
        self.__not_complete_order = "https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete"
        self.__ticket = Ticket()

    def ready_order(self):
        secret = self.__ticket.get_train_secret(self.__train_number)
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
        if result["status"] and result['data'] == '0':
            print("订单提交成功！")
        else:
            print(result)
            raise Exception("订单提交失败！系统自动退出...")

    def submit_order(self, init_params):
        params = {
            "cancel_flag": 2,
            "bed_level_order_num": "000000000000000000000000000000",
            "passengerTicketStr": init_params["passengers_str"],
            "oldPassengerStr": init_params["ticket_str"],
            "tour_flag": "dc",
            "randCode": "",
            "whatsSelect": 1,
            "sessionId": "",
            "sig": "",
            "scene": "nc_login",
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": init_params["REPEAT_SUBMIT_TOKEN"]
        }
        res = api.post(self.__check_order_info, data=params)
        result = res.json()
        if result["status"] and result["data"]["submitStatus"]:
            print("检查订单信息成功！")
            self.__ticket.query_left_tickets_info(init_params)
            if result["data"]["canChooseSeats"] == "Y":
                self.__ticket.choose_seat(init_params)
            return result["data"]
        else:
            print("检查订单信息失败！系统自动退出...")
            sys.exit(0)

    def get_request(self, submit_token):
        url = self.__get_order_info_url + "?random=" + str(
            int(time.time() * 1000)) + '&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=' + submit_token
        res = api.get(url)
        result = res.json()
        if result["status"] and result["data"]["queryOrderWaitTimeStatus"]:
            print("等待提交订单信息成功!")
            return result["data"]["requestId"]
        else:
            print(result)
            print('等待提交订单信息失败!系统自动退出...')
            sys.exit(0)

    def get_cached_order(self):
        params = {
            "_json_att": ""
        }
        res = api.post(self.__not_complete_order, data=params)
        result = res.json()
        if result["status"]:
            return result["data"]["orderCacheDTO"]
        else:
            print(result)
            print("获取缓存订单失败！系统自动退出...")
            sys.exit(0)

    def get_not_complete_order(self):
        params = {
            "_json_att": ""
        }
        res = api.post(self.__not_complete_order, data=params)
        result = res.json()
        if result["status"]:
            return result["data"]["orderDBList"]
        else:
            print("获取未完成失败！系统自动退出。。。")
            sys.exit(0)

    def check_order_successfully(self, request_id):
        cached_order = self.get_cached_order()
        cached_order_id = cached_order["requestId"]
        return cached_order_id == request_id
