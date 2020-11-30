# -*- coding: UTF-8 -*-
from src.core.auth.auth_context import AuthContext
from config import config
from src.core.ticket.order import Order
from src.core.tools.init_dc import InitDc
from src.core.auth.passenger import Passenger


def login():
    context = AuthContext(config)
    context.auth()


def generate_order():
    print("您预订的车次为：" + config.TRAIN_NUMBER + " 预订时间为：" + config.TRAIN_DATA)
    print("出发车站为：" + config.FROM_STATION)
    print("终点车站为：" + config.END_STATION)
    order = Order()
    order.ready_order()
    init_params = InitDc.get_params()
    passenger = Passenger(init_params["REPEAT_SUBMIT_TOKEN"])
    init_params["passengers_str"] = passenger.get_passengers_str()
    init_params["ticket_str"] = passenger.get_ticket_str()
    order.submit_order(init_params)
    request_id = order.get_request(init_params["REPEAT_SUBMIT_TOKEN"])
    is_successfully = order.check_order_successfully(request_id)
    if is_successfully:
        print("恭喜您购买车票成功，赶紧登陆网页版12306，到订单中心->火车票订单->未完成订单 去付款吧！")


def set_up():
    login()
    generate_order()
