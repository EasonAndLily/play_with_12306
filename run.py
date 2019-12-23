# -*- coding=utf-8 -*-
import argparse
import sys


def parser_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("operate", type=str, help="r: 运行抢票程序, t: 运行测试, c: 检测抢票环境配置")
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parser_arguments(sys.argv[1:])
    if args.operate == "r":
        print("开始抢票......")
    elif args.operate == "t":
        print("开始运行测试......")
    elif args.operate == "c":
        print("检测抢票环境配置......")
    else:
        print("不支持此参数，请运行python run.py -h查看支持的参数！")
