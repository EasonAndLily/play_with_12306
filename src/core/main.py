# -*- coding: UTF-8 -*-
import sys

import numpy

from src.core.auth.captcha import Captcha
from src.core.auth.basic import BasicAuth
from config import config
from src.core.ticket.order import Order
from src.core.tools.init_dc import InitDc
from src.core.auth.passenger import Passenger
from src.core.tools.utils import Utils


def login():
    captcha = Captcha()
    answer = captcha.run()
    aut = BasicAuth(answer)
    aut.login()
    app_data = aut.get_apptk()
    aut.validate_apptk(app_data)


def generate_order():
    print("您预订的车次为：" + config.TRAIN_NUMBER + " 预订时间为：" + config.TRAIN_DATA)
    print("出发车站为：" + config.FROM_STATION)
    print("终点车站为：" + config.END_STATION)
    order = Order()
    order.submit_order()
    init_params = InitDc.get_params()
    passenger = Passenger(init_params["REPEAT_SUBMIT_TOKEN"])
    init_params["passengers_str"] = passenger.get_passengers_str()
    init_params["ticket_str"] = passenger.get_ticket_str()
    order.check_order_info(init_params)
    check_order(order, init_params)
    print("恭喜您购买车票成功，赶紧登陆网页版12306，到订单中心->火车票订单->未完成订单 去付款吧！")


def check_order(order, init_params):
    status, order_id = order.check_order_wait_time(init_params["REPEAT_SUBMIT_TOKEN"])
    if status:
        if order_id is None:
            orders = order.get_not_complete_order()
            if len(orders) > 0:
                left_order = list(filter(lambda order: is_correct_order(order), orders))
                if len(left_order) == 1:
                    order_id = left_order["sequence_no"]
                    order.check_order_successfully(order_id, init_params["REPEAT_SUBMIT_TOKEN"])
                else:
                    print("未找到待付款订单，系统自动退出...")
                    sys.exit(0)
            else:
                print("未找到待付款订单，系统自动退出...")
                sys.exit(0)
        else:
            order.check_order_successfully(order_id, init_params["REPEAT_SUBMIT_TOKEN"])
    else:
        print("下单失败,系统自动退出...")
        sys.exit(0)


def is_correct_order(order):
    return order["train_code_page"] == config.TRAIN_NUMBER and numpy.array_equal(config.PASSENGERS, order[
        "array_passser_name_page"]) and Utils.is_today(order["order_date"])


def set_up():
    login()
    generate_order()
