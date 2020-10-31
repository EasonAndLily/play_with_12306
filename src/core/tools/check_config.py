from builtins import classmethod, Exception

from src.core.tools.station import Station
from src.core.tools.utils import Utils


class CheckConfig:
    def __init__(self, config):
        self.config = config

    @classmethod
    def is_correct_date(cls, date):
        if not Utils.validate_time_format(date):
            raise Exception("日期格式配置出错，请使用正确的日期格式，如：2020-02-29")
        if not Utils.check_time_in_correct_range(date):
            raise Exception("无法购买超出当前时间29天外的车票，请正确配置购票日期！")
        return True

    @classmethod
    def is_existing_station(cls, from_station, end_station):
        station = Station()
        if not station.has_this_station(from_station):
            raise Exception("不存在此出发车站，请重新配置！")
        if not station.has_this_station(end_station):
            raise Exception("不存在此到达车站，请重新配置！")
        return True

    @classmethod
    def check_username_password(cls, username, password):
        if username is None or len(username) == 0:
            raise Exception("登陆用户名不能为空，请正确配置密码！")
        if password is None or len(password) == 0:
            raise Exception("密码不能为空，请正确配置密码！")


    @classmethod
    def check_passengers(cls, passengers):
        if passengers is None or len(passengers) <= 0:
            raise Exception("乘车人未配置，请添加乘车人！")

    @classmethod
    def check_train_number(cls, train_number):
        if train_number is None or len(train_number) <= 0:
            raise Exception("列出编号不能为空，请配置需购买的列车号！")

    @classmethod
    def check_seat_type(cls, seat_type):
        if seat_type is None or len(seat_type) <= 0:
            raise Exception("座位编号不能为空，请配置需购买的座位类型！")
        if seat_type not in ["O", "M", "9", "3", "1", "4"]:
            raise Exception("座位编号配置不合法，请配置正确的座位类型编号！")

    def check(self):
        CheckConfig.check_username_password(self.config.USERNAME, self.config.PASSWORD)
        CheckConfig.check_passengers(self.config.PASSENGERS)
        CheckConfig.is_correct_date(self.config.TRAIN_DATA)
        CheckConfig.is_existing_station(self.config.FROM_STATION, self.config.END_STATION)
        CheckConfig.check_train_number(self.config.TRAIN_NUMBER)
        CheckConfig.check_seat_type(self.config.SEAT_TYPE)




