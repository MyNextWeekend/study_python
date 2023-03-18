# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 17:40
# @Author  : hejinhu
import os

Base_path = os.path.dirname(os.path.dirname(__file__))


def get_path(path):
    if path:
        res_path = os.path.join(Base_path, path)
    else:
        res_path = Base_path
    return res_path
