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
        TestBasicAuth.session.cookies = requests.utils.add_dict_to_cookiejar(TestBasicAuth.session.cookies, {
            "Cookie": "uamtk=szOraZkX5L7qqSCiRwE1fElVZafQ_GImvB8wf-87Ip4tyl1l0"})
        result = TestBasicAuth.aut.get_apptk()
        self.assertFalse(result["get_apptk_successful"])

    def test_validate_apptk(self):
        TestBasicAuth.session.cookies = requests.utils.add_dict_to_cookiejar(TestBasicAuth.session.cookies, {
            "Cookie": "uamtk=szOraZkX5L7qqSCiRwE1fElVZafQ_GImvB8wf-87Ip4tyl1l0"})
        result = TestBasicAuth.aut.validate_apptk("MmngS7iLqTdAWwXSl-DBpxVO6DrrOyGg4tjoOU9jifA1pl1l0")
        self.assertFalse(result["verify_successful"])
