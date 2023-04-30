# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 15:38
# @Author  : hejinhu
import datetime


def get_before_date(days: int = 0, today: datetime.date = None) -> datetime.date:
    """
    :param days: 往前推的天数
    :param today: 当前日期
    :return:
    """
    if today:
        now = today
    else:
        now = datetime.date.today()
    return now - datetime.timedelta(days=days)


def get_before_datetime(days: int = 0, today_time: datetime.datetime = None) -> datetime.datetime:
    """
    :param days: 往前推的天数
    :param today_time: 当前时间
    :return:
    """
    if today_time:
        now = today_time
    else:
        now = datetime.datetime.now()
    return now - datetime.timedelta(days=days)


if __name__ == '__main__':
    print(get_before_date(11, datetime.date(2000, 12, 12)))
    print(get_before_datetime(11, datetime.datetime(2000, 12, 12, 12, 12, 12)))
