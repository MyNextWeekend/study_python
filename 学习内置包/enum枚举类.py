# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 09:39
# @Author  : hejinhu
from enum import Enum, auto


class Param(Enum):
    aaa1 = auto()
    aaa2 = auto()
    aaa3 = 100
    aaa4 = auto()
    aaa5 = auto()


print(Param.__dict__)
print(dir(Param))
print(Param.aaa1.name, Param.aaa1.value)
print(Param.aaa2.name, Param.aaa2.value)
print(Param.aaa3.name, Param.aaa3.value)
print(Param.aaa4.name, Param.aaa4.value)
print(Param.aaa5.name, Param.aaa5.value)
