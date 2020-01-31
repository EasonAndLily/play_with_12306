# -*- coding: UTF-8 -*-
import sys
from unittest import TestCase

sys.path.append('../../../src')
from core.tools.init_dc import InitDc


class TestInitDc(TestCase):
    def test_get_params(self):
        params = InitDc.get_params()
        self.assertIsNotNone(params)
        self.assertIsNone(params["REPEAT_SUBMIT_TOKEN"])
        self.assertIsNone(params["key_check_isChange"])
        self.assertIsNone(params["leftTicketStr"])

    def test_parse_html_data(self):
        with open("init_data.html") as data:
            html_data = data.read()
            params = InitDc.parse_html_data(html_data)
            self.assertEqual(params["REPEAT_SUBMIT_TOKEN"], "9a6e391bf457fbcc2e1f0ec558cc9043")
            self.assertEqual(params["key_check_isChange"], "2B5F3EB00E0CC903F35D6373BB104B666583D8377A6A0A4D4140DF31")
            self.assertEqual(params["leftTicketStr"], "iogSLqCYhRZDSNyhZyO%2BsMsAFDY9M6Vkv82%2B6xu99w636w6K")
            self.assertEqual(params["tour_flag"], "dc")
            self.assertEqual(params["purpose_codes"], "00")
            self.assertEqual(params["train_location"], "P4")
            self.assertEqual(params["train_no"], "240000G41500")
            self.assertEqual(params["station_train_code"], "G415")
            self.assertEqual(params["from_station_telecode"], "VNP")
            self.assertEqual(params["to_station"], "SHH")
