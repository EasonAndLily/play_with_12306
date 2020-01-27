# -*- coding: UTF-8 -*-
import re


class InitDc(object):
    @classmethod
    def get_params(cls, session):
        url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        data = {
            "_json_att": ""
        }
        res = session.post(url, data=data)
        return cls.parse_html_data(res.text)

    @classmethod
    def parse_html_data(cls, html_data):
        repeat_submit_token = re.findall(re.compile("var globalRepeatSubmitToken = '(.*?)';", re.S), html_data)
        key_check_is_change = re.findall(re.compile("'key_check_isChange':'(.*?)',", re.S), html_data)
        left_ticket_str = re.findall(re.compile("'leftTicketStr':'(.*?)',", re.S), html_data)
        tour_flag = re.findall(re.compile(",'tour_flag':'(.*?)',", re.S), html_data)
        purpose_codes = re.findall(re.compile(",'purpose_codes':'(.*?)',", re.S), html_data)
        train_location = re.findall(re.compile(",'train_location':'(.*?)'", re.S), html_data)
        train_no = re.findall(re.compile(",'train_no':'(.*?)',", re.S), html_data)
        station_train_code = re.findall(re.compile(",'station_train_code':'(.*?)',", re.S), html_data)
        from_station_telecode = re.findall(re.compile(",'from_station_telecode':'(.*?)',", re.S), html_data)
        to_station = re.findall(re.compile(",'to_station':'(.*?)',", re.S), html_data)
        json_init_dc = {
            'REPEAT_SUBMIT_TOKEN': repeat_submit_token[0] if len(repeat_submit_token) > 0 else None,
            'key_check_isChange': key_check_is_change[0] if len(key_check_is_change) > 0 else None,
            'leftTicketStr': left_ticket_str[0] if len(left_ticket_str) > 0 else None,
            'tour_flag': tour_flag[0] if len(tour_flag) > 0 else None,
            'purpose_codes': purpose_codes[0] if len(purpose_codes) > 0 else None,
            'train_location': train_location[0] if len(train_location) > 0 else None,
            'train_no': train_no[0] if len(train_no) > 0 else None,
            'station_train_code': station_train_code[0] if len(station_train_code) > 0 else None,
            'from_station_telecode': from_station_telecode[0] if len(from_station_telecode) > 0 else None,
            'to_station': to_station[0] if len(to_station) > 0 else None
        }
        return json_init_dc
