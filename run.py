# -*- coding=utf-8 -*-
import sys
from config import config
from src.core.tools.check_config import CheckConfig
from src.core.main import set_up


def check_python_evn():
    if sys.version_info.major < 3:
        raise Exception("请使用Python 3.0 以上版本来运行此程序！")


def print_ticket_info():
    print("开始为您预订{}日从{}到{}的{}车票。。。".format(config.TRAIN_DATA, config.FROM_STATION, config.END_STATION,
                                           config.TRAIN_NUMBER))


if __name__ == '__main__':
    try:
        check_python_evn()
        check_config = CheckConfig(config)
        check_config.check()
        print_ticket_info()
    except Exception as ex:
        print(ex)
        exit(0)
    set_up()
