# -*- coding: UTF-8 -*-
import sys

sys.path.append('../../core')
from tools.generate_headers import GenerateHeaders
from ticket import Ticket
from station import Station


class Order(object):
    def __init__(self, train_date, from_station_name, to_station_name):
        self.__train_date = train_date
        self.__from_station_name = from_station_name
        self.__to_station_name = to_station_name
        self.__headers = GenerateHeaders.get_headers()

    def submit_order(self, session, train_number):
        station = Station()
        from_station = station.get_stations_keys_values()[self.__from_station_name]
        end_station = station.get_stations_keys_values()[self.__to_station_name]
        ticket = Ticket(from_station, end_station, self.__train_date)
        secret = ticket.get_train_secret(session, train_number)
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
        url = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
        res = session.post(url, data=data, headers=self.__headers)
        print res.text
        return res.json()

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
            print "Check order successfully!"
            return result["data"]
        else:
            print "Check Order Failed!"
            return False

