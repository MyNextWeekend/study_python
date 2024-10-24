# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 09:39
# @Author  : MyNextWeekend
from enum import Enum, auto, Flag, StrEnum


class Param(Enum):
    """
    枚举类
    """
    RED = auto()  # 1
    ORANGE = auto()  # 2
    YELLOW = 100  # 100
    GREEN = auto()  # 101
    BLUE = auto()  # 102
    PURPLE = auto()  # 103


# class ColorParam(str, Enum): # 字符串枚举
class ColorParam(StrEnum):
    """
    枚举类
    """
    RED = auto()
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"


class Color(Flag):
    """
    区别与Enum 主要可以做到判断一个具体枚举 是否存在一个枚举集合中
    """
    RED = auto()  # 1 = 2^0
    ORANGE = auto()  # 2 = 2^1
    GREEN = auto()  # 4 = 2^2
    BLUE = auto()  # 8 = 2^3
    PURPLE = auto()  # 16 = 2^4


if __name__ == '__main__':
    print(Param.__dict__)
    print(dir(Param))

    print(Param.RED.name, Param.RED.value)
    print(Param.ORANGE.name, Param.ORANGE.value)
    print(Param.YELLOW.name, Param.YELLOW.value)
    print(Param.GREEN.name, Param.GREEN.value)
    print(Param.BLUE.name, Param.BLUE.value)

    print(f"输入的值是red:{ColorParam.RED == 'red'}")
    print(f"有一个枚举是:{ColorParam.RED.value}")

    print("=" * 20)
    print(Color.__dict__)
    print(dir(Color))
    choose_color = Color.RED
    good_colors = Color.RED | Color.GREEN | Color.ORANGE
    print(choose_color in good_colors)  # 判断一个枚举是否在已知的枚举集合中
