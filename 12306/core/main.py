# -*- coding: UTF-8 -*-
import json

import requests
from auth.captcha import Captcha
from auth.basic import BasicAuth
# from ticket.order import Order
# from tools.generate_headers import GenerateHeaders
# from tools.init_dc import InitDc
# from auth.passenger import Passenger
# from ticket.ticket import Ticket


def login():
    captcha = Captcha()
    answer = captcha.run()
    aut = BasicAuth(answer)
    aut.login()
    app_data = aut.get_apptk()
    aut.validate_apptk(app_data)


# def generate_order(session, train_date, from_station_name, to_station_name, train_number):
#     print "Scheduling train " + train_number + " date is " + train_date
#     print "From: " + from_station_name
#     print "To: " + to_station_name
#     order = Order(train_date, from_station_name, to_station_name)
#     result = order.submit_order(session, train_number)
#     if result["status"] and result['data'] == 'N':
#         print "submit order request successfully!"
#         return True
#     else:
#         print "submit order request failed!"
#         return False


# def generate_init_params(session):
#     params = InitDc.get_params(session)
#     print params["REPEAT_SUBMIT_TOKEN"]
#     passengers = Passenger(params["REPEAT_SUBMIT_TOKEN"]).get_passenger(session, config["passengers"])
#     ticket_str = ""
#     passenger_str = ""
#     for passenger in passengers:
#         passenger_str += "" if passenger_str == "" else "_"
#         passenger_str += 'O,' + passenger['passenger_flag'] + ',' + passenger['passenger_type'] + ',' + passenger[
#             'passenger_name'] + ',' + passenger['passenger_id_type_code'] + ',' + passenger['passenger_id_no'] + ',' + \
#                          passenger['mobile_no'] + ',N' + passenger["allEncStr"]
#         ticket_str += passenger['passenger_name'] + ',' + passenger['passenger_id_type_code'] + ',' + passenger[
#             'passenger_id_no'] + ',1_'
#     params["passenger_str"] = passenger_str
#     params["ticket_str"] = ticket_str
#     return params
#
#
# def can_order_left_tickets(session, init_params, config):
#     left_tickets_info = Ticket.query_left_tickets_info(session, init_params, config["seat_type"], config["date"])
#     if left_tickets_info is not None:
#         print "There are " + left_tickets_info["left_tickets"] + " tickets left for your current purchase seat type"
#         print "There are currently " + left_tickets_info["queue_count"] + " people in line"
#         return True
#     else:
#         print "No left tickets for this seat type..."
#         return False
#
#
# def choose_seats(session, init_params, seats):
#     chose_seat = Ticket.choose_seat(session, init_params, seats)
#     if chose_seat:
#         print "Choose Seats successfully!"
#     else:
#         print "Choose Seats failed"


if __name__ == '__main__':
    login()
