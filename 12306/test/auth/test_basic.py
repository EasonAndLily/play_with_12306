import binascii
from unittest import TestCase
import sys
import base64

sys.path.append('../../../12306')
from core.auth.basic import BasicAuth


def is_base64(s):
    try:
        base64.decodestring(s)
        return True
    except binascii.Error:
        return False


class TestBasicAuth(TestCase):
    def test_get_captcha(self):
        image_data = BasicAuth.get_captcha()
        self.assertIsNotNone(image_data)
        self.assertTrue(is_base64(image_data))

    def test_save_captcha(self):
        import os
        file_path = os.path.dirname(os.path.abspath(__file__))
        BasicAuth.save_captcha(file_path + "/", "captcha.jpg")
        import os
        self.assertTrue(os.path.isfile('captcha.jpg'))
