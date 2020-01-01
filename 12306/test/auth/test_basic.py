import binascii
from unittest import TestCase
import sys
import base64

import requests

sys.path.append('../../../12306')
from core.auth.basic import BasicAuth


class TestBasicAuth(TestCase):
    session = requests.session()
    aut = BasicAuth(session, "test", "test", "35,35")

    def test_login(self):
        result = TestBasicAuth.aut.login()
        self.assertFalse(result["is_login"])

    def test_get_apptk(self):
        TestBasicAuth.session.cookies = requests.utils.add_dict_to_cookiejar(TestBasicAuth.session.cookies, {
            "Cookie": "uamtk=szOraZkX5L7qqSCiRwE1fElVZafQ_GImvB8wf-87Ip4tyl1l0"})
        result = TestBasicAuth.aut.get_apptk()
        self.assertFalse(result["get_apptk_successful"])

    def test_validate_apptk(self):
        TestBasicAuth.session.cookies = requests.utils.add_dict_to_cookiejar(TestBasicAuth.session.cookies, {
            "Cookie": "uamtk=szOraZkX5L7qqSCiRwE1fElVZafQ_GImvB8wf-87Ip4tyl1l0"})
        result = TestBasicAuth.aut.validate_apptk("MmngS7iLqTdAWwXSl-DBpxVO6DrrOyGg4tjoOU9jifA1pl1l0")
        self.assertTrue(result["verify_successful"])
