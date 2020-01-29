import base64
import binascii
import sys
from unittest import TestCase

sys.path.append('../../../12306')
from core.auth.captcha import Captcha


def is_base64(s):
    try:
        base64.decodebytes(s)
        return True
    except binascii.Error:
        return False


class TestCaptcha(TestCase):

    def test_get_captcha(self):
        image_data = Captcha.get_captcha()
        self.assertIsNotNone(image_data)
        self.assertTrue(is_base64(image_data.encode()))

    def test_check_captcha(self):
        image_data = Captcha.get_captcha()
        answer = Captcha.verify_captcha_auto(image_data)
        result = Captcha.check_captcha(answer)
        self.assertTrue(result["is_successful"])
