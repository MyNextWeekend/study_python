# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 09:39
# @Author  : hejinhu
from enum import Enum, auto


class Param(Enum):
    red = auto()  # 1
    orange = auto()  # 2
    yellow = 100  # 100
    green = auto()  # 101
    blue = auto()  # 102
    purple = auto()  # 103


if __name__ == '__main__':
    print(Param.__dict__)
    print(dir(Param))
    print(Param.red.name, Param.red.value)
    print(Param.orange.name, Param.orange.value)
    print(Param.yellow.name, Param.yellow.value)
    print(Param.green.name, Param.green.value)
    print(Param.blue.name, Param.blue.value)
