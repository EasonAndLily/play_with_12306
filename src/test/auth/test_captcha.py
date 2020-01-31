import base64
import binascii
import sys
from unittest import TestCase

sys.path.append('../../../src')
from core.auth.captcha import Captcha
from core.tools.utils import Utils


def is_base64(s):
    try:
        base64.decodebytes(s)
        return True
    except binascii.Error:
        return False


class TestCaptcha(TestCase):
    def setUp(self):
        self.captcha = Captcha()

    def test_get_captcha(self):
        image_data = self.captcha.get_captcha()
        self.assertIsNotNone(image_data)
        self.assertTrue(is_base64(image_data.encode()))

    def test_check_captcha(self):
        image_data = self.captcha.get_captcha()
        image_indexes = Captcha.verify_captcha_auto(image_data)
        answer = Utils.get_captcha_answer(image_indexes)
        result = self.captcha.check_captcha(answer)
        self.assertTrue(result)
