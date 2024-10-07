# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 17:40
# @Author  : MyNextWeekend
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))


def get_path(path: str = '') -> str:
    """
    path：相对路径，如果为空，则返回项目根目录
    """
    if not path:
        return BASE_PATH
    if '/' in path:
        path = os.sep.join(path.split('/'))
    if '\\' in path:
        path = os.sep.join(path.split('\\'))
    if not path.startswith(os.sep):
        path = os.sep + path
    return BASE_PATH + path
