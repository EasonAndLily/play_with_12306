# -*- coding: UTF-8 -*-
import json

import requests
from auth.captcha import Captcha
from auth.basic import BasicAuth
from ticket.order import Order
from tools.generate_headers import GenerateHeaders


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


if __name__ == '__main__':
    session = requests.session()
    config = read_config()
    verify_captcha = Captcha.run(session)
    if verify_captcha["is_successful"]:
        handle_session(session)
        config = read_config()
        result = login(verify_captcha["answer"], config["username"], config["password"])
        if result:
            generate_order(session, config["date"], config["from_station"], config["to_station"],
                           config["train_number"])
