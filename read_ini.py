# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 22:09
# @Author  : hejinhu
import configparser

from Utils.path import get_path


def get_args(file):
    cfg = configparser.RawConfigParser()
    cfg.read(file, encoding='utf-8')
    return cfg


if __name__ == '__main__':
    file_path = get_path('Config/config.ini')
    f = get_args(file_path)
    # 如果key不存在就返回fallback
    user = f.get('mysql', 'user', fallback='')
    print(user)
