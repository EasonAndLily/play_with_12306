import binascii
from unittest import TestCase
import sys
import base64

import requests

sys.path.append('../../../12306')
from core.auth.basic import BasicAuth


class TestBasicAuth(TestCase):

    def test_login(self):
        session = requests.session()
        aut = BasicAuth(session, "test", "test", "35,35")
        result = aut.login()
        self.assertFalse(result["is_login"])
