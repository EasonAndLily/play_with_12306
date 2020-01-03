# -*- coding: UTF-8 -*-
import datetime
import sys
from unittest import TestCase

sys.path.append('../../../12306')
from core.ticket.ticket import Ticket


class TestTicket(TestCase):
    def test_query_left_tickets(self):
        date = str(datetime.date.today() + datetime.timedelta(days=1))
        ticket = Ticket("WHN", "DSJ", date)
        left_tickets = ticket.query_left_tickets()
        self.assertEqual(len(left_tickets), 4)
        self.assertEqual(left_tickets[0]["trains_number"], "K226")
        self.assertEqual(left_tickets[0]["from_station"], u"武昌")
        self.assertEqual(left_tickets[0]["end_station"], u"定西")
        self.assertEqual(left_tickets[0]["start_time"], "09:46")
        self.assertEqual(left_tickets[0]["arrive_time"], "07:11")
        self.assertEqual(left_tickets[0]["duration"], "21:25")
        self.assertEqual(left_tickets[0]["business_class"], "")
        self.assertEqual(left_tickets[0]["first_class"], "")
        self.assertEqual(left_tickets[0]["second_class"], "")
        self.assertEqual(left_tickets[0]["advance_soft_sleeper"], "")
        self.assertEqual(left_tickets[0]["bullet_train_sleeper"], "")
        self.assertIsNotNone(left_tickets[0]["soft_sleeper"])
        self.assertIsNotNone(left_tickets[0]["hard_sleeper"])
        self.assertEqual(left_tickets[0]["soft_seat"], "")
        self.assertIsNotNone(left_tickets[0]["hard_seat"])
        self.assertIsNotNone(left_tickets[0]["none_seat"])