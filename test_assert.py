# -*- coding: utf-8 -*-
# @Time    : 2022/12/16 13:05
# @Author  : hejinhu
assert 1 == 1

try:
    assert 1 == 2, "66666"
except AssertionError as e:
    print(f'11111{e}')
