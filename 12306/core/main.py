import json

import requests
from auth.captcha import Captcha
from auth.basic import BasicAuth
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
                print verify_data["username"] + " login successfully!"
                return verify_data["apptk"]
    else:
        print "Please check captcha again!"


if __name__ == '__main__':
    session = requests.session()
    handle_session(session)
    config = read_config()
    apptk = login(session, config["username"], config["password"])
    if apptk is not None:
        print apptk
