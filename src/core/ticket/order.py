# -*- coding: UTF-8 -*-
import sys
import time

from config import config
from src.core.tools.api_request import api
from .ticket import Ticket


class Order(object):
    def __init__(self):
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

    def submit_order(self):
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
        if result["status"] and result['data'] == 'N':
            print("订单提交成功！")
        else:
            print("订单提交失败！系统自动退出...")
            sys.exit(0)

    def check_order_info(self, init_params):
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

    def check_order_wait_time(self, submit_token):
        url = self.__get_order_info_url + "?random=" + str(
            int(time.time() * 1000)) + '&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=' + submit_token
        res = api.get(url)
        result = res.json()
        print(result)
        if result["status"] and result["data"]["queryOrderWaitTimeStatus"]:
            print("等待提交订单信息成功!")
            order_id = result["data"]["orderId"]
            if result["data"]["waitTime"] <= 0 and result["data"]["requestId"] is not None and order_id is None:
                return True, order_id
            elif result["data"]["waitTime"] > 0:
                time.sleep(result["data"]["waitTime"])
                res = api.get(url)
                waited_result = res.json()
                if waited_result["status"] and waited_result["data"]["queryOrderWaitTimeStatus"]:
                    return True, waited_result["data"]["orderId"]
            else:
                print("等待提交订单信息失败!系统自动退出...")
                sys.exit(0)
            if "msg" in result["data"].keys():
                print(result["data"]["msg"])
        else:
            print('等待提交订单信息失败!系统自动退出...')
            sys.exit(0)

    def get_not_complete_order(self):
        params = {
            "_json_att": ""
        }
        res = api.post(self.__not_complete_order, data=params)
        result = res.json()
        print(result)
        if result["status"]:
            return result["data"]["orderDBList"]
        else:
            print("获取未完成失败！系统自动退出。。。")
            sys.exit(0)

    def check_order_successfully(self, order_id, submit_token):
        params = {
            'orderSequence_no': order_id,
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': submit_token
        }
        res = api.post(self.__check_order_for_queue, data=params)
        print(res.text)
        result = res.json()
        if result['status'] and result['data']['submitStatus']:
            print('下单成功!')
        else:
            print("下单失败！系统自动退出.....")
            sys.exit(0)
