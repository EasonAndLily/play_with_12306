# -*- coding=utf-8 -*-
import sys
from config import config
from src.core.tools.check_config import CheckConfig


def check_python_evn():
    if sys.version_info.major < 3:
        raise Exception("请使用Python 3.0 以上版本来运行此程序！")


if __name__ == '__main__':
    try:
        check_python_evn()
        check_config = CheckConfig(config)
        check_config.check()
    except Exception as ex:
        print(ex)
        exit(0)
    # check_python_evn()
    # check_config_info()
    # set_up()
