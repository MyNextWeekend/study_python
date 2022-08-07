# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 00:02
# @Author  : hejinhu
import os

a = os.path.abspath(os.path.dirname(__file__))
print(a.split('study')[0])
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.getcwd())