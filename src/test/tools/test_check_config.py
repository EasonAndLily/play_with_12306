# coding=utf-8
from builtins import Exception, str
from unittest import TestCase
from src.core.tools.check_config import CheckConfig
from src.core.tools.utils import Utils


class TestCheckConfig(TestCase):

    def test_config_date_format(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.is_correct_date("2020/02/28")
        self.assertTrue('日期格式配置出错，请使用正确的日期格式，如：2020-02-29' in str(context.exception))

    def test_config_date_within_next_month(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.is_correct_date("2020-02-28")
        self.assertTrue('无法购买超出当前时间29天外的车票，请正确配置购票日期！' in str(context.exception))

    def test_correct_date(self):
        today = Utils.current_date()
        result = CheckConfig.is_correct_date(today)
        self.assertTrue(result)

    def test_not_existing_from_station(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.is_existing_station("东湖", "武昌")
        self.assertTrue('不存在此出发车站，请重新配置！' in str(context.exception))

    def test_not_existing_end_station(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.is_existing_station("武昌", "东湖")
        self.assertTrue('不存在此到达车站，请重新配置！' in str(context.exception))

    def test_existing_stations(self):
        result = CheckConfig.is_existing_station("武昌", "兰州")
        self.assertTrue(result)

    def test_check_username_is_none(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.check_username_password(None, "123")
        self.assertTrue('登陆用户名不能为空，请正确配置密码！' in str(context.exception))

    def test_check_password_is_none(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.check_username_password("123", "")
        self.assertTrue('密码不能为空，请正确配置密码！' in str(context.exception))

    def test_check_passengers(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.check_passengers(None)
        self.assertTrue('乘车人未配置，请添加乘车人！' in str(context.exception))

    def test_check_train_number(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.check_train_number("")
        self.assertTrue('列出编号不能为空，请配置需购买的列车号！' in str(context.exception))

    def test_check_seat_type_not_null(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.check_seat_type("")
        self.assertTrue('座位编号不能为空，请配置需购买的座位类型！' in str(context.exception))

    def test_check_seat_type_not_correct(self):
        with self.assertRaises(Exception) as context:
            CheckConfig.check_seat_type("8")
        self.assertTrue('座位编号配置不合法，请配置正确的座位类型编号！' in str(context.exception))