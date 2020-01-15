# -*- coding: UTF-8 -*-
import sys
from unittest import TestCase

import requests

sys.path.append('../../../12306')
from core.ticket.order import Order


class TestOrder(TestCase):

    def test_submit_order(self):
        train_secret = "sFOfLAQDylybAyKEw1G92dfDqJ8wbuVB25fXQ7FATQ3d4tJxJarUbhspw/j4HWtHqcWCWS0ZkvOik4wJkgBv+C4/OdOSfABJ5hG8A1JRu9FwOmqmLdVfVASzbhPTlUTRg+fKNbP4hgSC8hWM+kMVYHAxjgcrwpJxc2/qXNEu+FNG7btwzjuLCYx6KQmViQ1ZcAyP0jidlhyCQGTgbACEBTEcduhJesPBOuDjgFkLeFOR02wA6P7OtnmGYRmSQQP9Eeu/Jyr/XeoFT2XXbfqHiOVC66z7m1Rk7/sB+zWOAoR839EMWrkBdQ==";
        order = Order(train_secret, "2020-02-09", u"银川", u"武汉")
        order.submit_order(requests.session())
