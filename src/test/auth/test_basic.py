from unittest import TestCase

from src.core.auth.basic import BasicAuth
from src.core.auth.captcha import Captcha
from config import config


class TestBasicAuth(TestCase):
    def setUp(self):
        self.captcha = Captcha()
        answer = self.captcha.run(config)
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
