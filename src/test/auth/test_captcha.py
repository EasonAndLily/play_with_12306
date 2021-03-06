from unittest import TestCase
from unittest.mock import MagicMock
from src.core.tools.api_request import api
from src.core.auth.captcha import Captcha
from src.core.tools.utils import Utils


class TestCaptcha(TestCase):
    def setUp(self):
        self.captcha = Captcha()
        result = Utils.get_json_data_from_file('./', 'captcha.json')
        api.get = MagicMock()
        api.get().json = MagicMock(return_value=result)

    def test_get_captcha(self):
        image_data = self.captcha.get_captcha()
        self.assertIsNotNone(image_data)
        self.assertTrue(Utils.is_base64(image_data.encode()))

    def test_check_captcha_auto(self):
        image_data = Utils.get_json_data_from_file('./', 'captcha.json')
        image_indexes = Captcha.verify_captcha_auto(image_data["image"])
        self.assertEqual(image_indexes, [2, 4])
