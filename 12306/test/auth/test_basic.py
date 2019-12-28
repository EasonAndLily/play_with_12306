import binascii
from unittest import TestCase
import sys
import base64

sys.path.append('../../../12306')
from core.auth.basic import BasicAuth


class TestBasicAuth(TestCase):

    def test_login(self):
        basic_auth = BasicAuth("15342349100", "232699ljh")
        res = basic_auth.login()
        print res.text
        self.assertEqual(res.status_code, 200)
