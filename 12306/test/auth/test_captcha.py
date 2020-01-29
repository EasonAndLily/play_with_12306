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

    def test_save_captcha(self):
        import os
        file_path = os.path.dirname(os.path.abspath(__file__))
        Captcha.save_captcha(Captcha.get_captcha(), file_path + "/", "captcha.jpg")
        self.assertTrue(os.path.isfile('captcha.jpg'))

    def test_check_captcha(self):
        Captcha.get_captcha()
        images_number = [2, 4, 6]
        result = Captcha.check_captcha(images_number)
        self.assertFalse(result["is_successful"])
