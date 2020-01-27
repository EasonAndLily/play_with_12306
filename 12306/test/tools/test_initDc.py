# -*- coding: UTF-8 -*-
import sys
from unittest import TestCase

import requests

sys.path.append('../../../12306')
from core.tools.init_dc import InitDc


class TestInitDc(TestCase):
    def test_get_params(self):
        params = InitDc.get_params(requests.session())
        self.assertIsNotNone(params)
        self.assertIsNone(params["REPEAT_SUBMIT_TOKEN"])
        self.assertIsNone(params["key_check_isChange"])
        self.assertIsNone(params["leftTicketStr"])
