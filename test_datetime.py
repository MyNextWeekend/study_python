# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 17:12
# @Author  : hejinhu
import datetime


def get_time(day_num=0):
    now = datetime.datetime.now()
    day = datetime.timedelta(day_num)
    return now - day


if __name__ == '__main__':
    get_time(2)
