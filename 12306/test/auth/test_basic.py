from unittest import TestCase
import sys
import requests

sys.path.append('../../../12306')
from core.auth.basic import BasicAuth
from core.auth.captcha import Captcha


class TestBasicAuth(TestCase):
    def setUp(self):
        self.captcha = Captcha()
        answer = self.captcha.run()
        self.auth = BasicAuth(answer)

    def test_login(self):
        result = self.auth.login()
        self.assertIsNotNone(result)

    def test_get_apptk(self):
        self.auth.login()
        apptk = self.auth.get_apptk()
        self.assertIsNotNone(apptk)

    def test_validate_apptk(self):
        self.auth.login()
        apptk = self.auth.get_apptk()
        new_apptk = self.auth.validate_apptk(apptk)
        self.assertIsNotNone(new_apptk)
