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
    session.cookies = requests.utils.add_dict_to_cookiejar(session.cookies, {
        "Cookie": "RAIL_DEVICEID=" + expiration_device["RAIL_DEVICEID"]})


def login(session, username, password):
    result = Captcha.run(session)
    if result["is_successful"]:
        aut = BasicAuth(session, username, password, result["answer"])
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


def generate_order(session, train_data, from_station_name, to_station_name, train_number):
    order = Order(train_data, from_station_name, to_station_name)
    order.submit_order(session, train_number)


if __name__ == '__main__':
    session = requests.session()
    handle_session(session)
    config = read_config()
    result = login(session, config["username"], config["password"])
    if result:
        generate_order(session, config["date"], config["from_station"], config["to_station"], config["train_number"])

