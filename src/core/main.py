# -*- coding: UTF-8 -*-
from auth.captcha import Captcha
from auth.basic import BasicAuth
from config import config
from ticket.order import Order
from tools.init_dc import InitDc
from auth.passenger import Passenger


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
    order_id = order.get_order_id(init_params["REPEAT_SUBMIT_TOKEN"])
    if order_id is not None:
        order.check_order_successfully(order_id, init_params["REPEAT_SUBMIT_TOKEN"])
    print("恭喜您购买车票成功，赶紧登陆网页版12306，到订单中心->火车票订单->未完成订单 去付款吧！")


if __name__ == '__main__':
    login()
    generate_order()
