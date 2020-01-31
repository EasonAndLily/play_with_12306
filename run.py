# -*- coding=utf-8 -*-
import argparse
import sys
from config import config
from src.core.tools.utils import Utils
from src.core.tools.station import Station
from src.core.main import set_up


def check_python_evn():
    if sys.version_info.major < 3:
        print("请使用Python 3.0 以上版本来运行此程序！")
        sys.exit(0)


def check_config_info():
    if not Utils.validate_time_format(config.TRAIN_DATA):
        print("日期格式配置出错，请使用正确的日期格式，如：2020-02-29")
        sys.exit(0)
    if not Utils.check_time_in_correct_range(config.TRAIN_DATA):
        print("配置的出发日期不在正确的范围内，请配置当前一个月以内的日期！")
        sys.exit(0)

    station = Station()
    if not station.has_this_station(config.FROM_STATION) and not station.has_this_station(config.END_STATION):
        print("出发站或抵达站配置有误！")
        sys.exit(0)

    if config.USERNAME is None or config.PASSENGERS is None:
        print("登陆用户名或者密码不能为空！")
        sys.exit(0)

    if config.PASSENGERS is None or len(config.PASSENGERS) <= 0:
        print("乘车人未配置，请添加乘车人！")
        sys.exit(0)


if __name__ == '__main__':
    check_python_evn()
    check_config_info()
    set_up()
