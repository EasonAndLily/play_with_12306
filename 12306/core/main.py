# -*- coding: UTF-8 -*-
import json

import requests
from auth.captcha import Captcha
from auth.basic import BasicAuth
from ticket.order import Order
from tools.generate_headers import GenerateHeaders
from tools.init_dc import InitDc
from auth.passenger import Passenger
from ticket.ticket import Ticket


def read_config():
    with open("../../config/config.json", "r") as f:
        return json.load(f)


def handle_session(session):
    expiration_device = GenerateHeaders.get_rail_expiration_device_id()
    expiration = "RAIL_EXPIRATION=" + expiration_device["RAIL_EXPIRATION"] + ";"
    deviceid = "RAIL_DEVICEID=" + expiration_device["RAIL_DEVICEID"] + ";"
    session.cookies = requests.utils.add_dict_to_cookiejar(session.cookies, {"Cookie": expiration + deviceid})


def login(answer, username, password):
    aut = BasicAuth(session, username, password, answer)
    aut.login()
    app_data = aut.get_apptk()
    if app_data["get_apptk_successful"]:
        verify_data = aut.validate_apptk(app_data["newapptk"])
        if verify_data["verify_successful"]:
            session.cookies = requests.utils.add_dict_to_cookiejar(session.cookies, {
                "Cookie": "tk=" + verify_data["apptk"] + ";"
            })
            print verify_data["username"] + " login successfully!"
            return True
    else:
        print "Please check captcha again!"
        return False


def generate_order(session, train_date, from_station_name, to_station_name, train_number):
    print "Scheduling train " + train_number + " date is " + train_date
    print "From: " + from_station_name
    print "To: " + to_station_name
    order = Order(train_date, from_station_name, to_station_name)
    result = order.submit_order(session, train_number)
    if result["status"] and result['data'] == 'N':
        print "submit order request successfully!"
        return True
    else:
        print "submit order request failed!"
        return False


def generate_init_params(session):
    params = InitDc.get_params(session)
    passengers = Passenger(params["REPEAT_SUBMIT_TOKEN"]).get_passenger(session, config["passengers"])
    ticket_str = ""
    passenger_str = ""
    for passenger in passengers:
        passenger_str += "" if passenger_str == "" else "_"
        passenger_str += 'O,' + passenger['passenger_flag'] + ',' + passenger['passenger_type'] + ',' + passenger[
            'passenger_name'] + ',' + passenger['passenger_id_type_code'] + ',' + passenger['passenger_id_no'] + ',' + \
                         passenger['mobile_no'] + ',N' + passenger["allEncStr"]
        ticket_str += passenger['passenger_name'] + ',' + passenger['passenger_id_type_code'] + ',' + passenger[
            'passenger_id_no'] + ',1_'
    params["passenger_str"] = passenger_str
    params["ticket_str"] = ticket_str
    return params


def can_order_left_tickets(session, init_params, config):
    left_tickets_info = Ticket.query_left_tickets_info(session, init_params, config["seat_type"], config["date"])
    if left_tickets_info is not None:
        print "There are " + left_tickets_info["left_tickets"] + " tickets left for your current purchase seat type"
        print "There are currently " + left_tickets_info["queue_count"] + " people in line"
        return True
    else:
        print "No left tickets for this seat type..."
        return False


if __name__ == '__main__':
    session = requests.session()
    config = read_config()
    verify_captcha = Captcha.run(session)
    if verify_captcha["is_successful"]:
        handle_session(session)
        config = read_config()
        result = login(verify_captcha["answer"], config["username"], config["password"])
        if result:
            is_successfully = generate_order(session, config["date"], config["from_station"], config["to_station"],
                                             config["train_number"])
            if is_successfully:
                init_params = generate_init_params(session)
                Order.check_order_info(session, init_params["passenger_str"], init_params["ticket_str"],
                                       init_params["REPEAT_SUBMIT_TOKEN"])
                can_order_left_tickets(session, init_params, config)
