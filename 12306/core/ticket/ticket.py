# -*- coding: UTF-8 -*-
import datetime
import json
import requests
import sys

sys.path.append('../../core')
from config import config
from tools.api_request import api
from tools.station import Station


class Ticket(object):
    def __init__(self):
        self.__station = Station()
        self.__from_station = self.__station.get_station_key_by_values(config.FROM_STATION)
        self.__end_station = self.__station.get_station_key_by_values(config.END_STATION)
        self.__train_date = config.TRAIN_DATA
        self.__query_left_tickets_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ"
        self.__query_queue_count = "https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"

    def query_left_tickets(self):
        url = self.__query_left_tickets_url + "?leftTicketDTO.train_date=" + self.__train_date + "&leftTicketDTO.from_station=" + \
              self.__from_station + "&leftTicketDTO.to_station=" + self.__end_station + "&purpose_codes=ADULT"
        res = api.get(url)
        data = res.json()
        if data["httpstatus"] == 200:
            return self.parse_string_array_to_tickets(data["data"]["result"], data["data"]["map"])

    @classmethod
    def parse_string_array_to_tickets(cls, data, station_map):
        tickets = []
        for item in data:
            info = item.split("|")
            result = dict()
            result.update({"trains_number": info[3]})
            result.update({"train_secret": requests.utils.unquote(info[0])})
            result.update({"from_station": station_map[info[6]]})
            result.update({"end_station": station_map[info[7]]})
            result.update({"start_time": info[8]})
            result.update({"arrive_time": info[9]})
            result.update({"duration": info[10]})
            result.update({"business_class": info[32] or info[25]})
            result.update({"first_class": info[31]})
            result.update({"second_class": info[30]})
            result.update({"advance_soft_sleeper": info[21]})
            result.update({"bullet_train_sleeper": info[27]})
            result.update({"soft_sleeper": info[23]})
            result.update({"hard_sleeper": info[28]})
            result.update({"soft_seat": info[24]})
            result.update({"hard_seat": info[29]})
            result.update({"none_seat": info[26]})
            tickets.append(result)
        return tickets

    def can_book_specified_ticket(self, train_numbers, seat_info):
        tickets = self.query_left_tickets()
        specified_ticket = list(filter(lambda item: item["trains_number"] == train_numbers, tickets))
        return len(specified_ticket) > 0 and specified_ticket[0][seat_info] != "" \
               and specified_ticket[0][seat_info] != u"无"

    def get_train_secret(self, train_numbers):
        tickets = self.query_left_tickets()
        specified_ticket = list(filter(lambda item: item["trains_number"] == train_numbers, tickets))
        return specified_ticket[0]["train_secret"]

    def query_left_tickets_info(self, init_params):
        params = {
            "train_date": datetime.datetime.strptime(config.TRAIN_DATA, '%Y-%m-%d').strftime(
                "%a %b %d %Y %H:%M:%S GMT+0800 (中国标准时间)"),
            "train_no": init_params["train_no"],
            "stationTrainCode": init_params["station_train_code"],
            "seatType": config.SEAT_TYPE,
            "fromStationTelecode": init_params["from_station_telecode"],
            "toStationTelecode": init_params["to_station"],
            "leftTicket": init_params["leftTicketStr"],
            "purpose_codes": init_params["purpose_codes"],
            "train_location": init_params["train_location"],
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": init_params["REPEAT_SUBMIT_TOKEN"]
        }
        res = api.post(self.__query_queue_count, data=params)
        result = res.json()
        if result["status"]:
            print("您所选的座位还剩余" + result["data"]["ticket"] + "张车票")
        else:
            print("获取余票失败！系统自动退出.....")
            sys.exit(0)

    @staticmethod
    def choose_seat(session, init_params, choose_seats):
        url = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
        params = {
            "passengerTicketStr": init_params["passenger_str"],
            "oldPassengerStr": init_params["ticket_str"],
            "randCode": "",
            "purpose_codes": init_params["purpose_codes"],
            "key_check_isChange": init_params["key_check_isChange"],
            "leftTicketStr": init_params["leftTicketStr"],
            "train_location": init_params["train_location"],
            "choose_seats": choose_seats,
            "seatDetailType": 000,
            "whatsSelect": 1,
            "roomType": 00,
            "dwAll": "N",
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": init_params["REPEAT_SUBMIT_TOKEN"]
        }
        res = session.post(url, data=params)
        print
        res.text
        result = res.json()
        return result["status"] and result["data"]["submitStatus"]
