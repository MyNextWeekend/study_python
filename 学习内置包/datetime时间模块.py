# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 15:38
# @Author  : MyNextWeekend
import datetime
import time


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


def get_before_time(today_time: datetime.datetime = None,
                    day: int = 0, hour: int = 0, minute: int = 0, second: int = 0) -> datetime.datetime:
    """
    :param today_time: 当前时间
    :param day: 往前的天数
    :param hour: 往前的小时数
    :param minute: 往前的分钟数
    :param second: 往前的秒数
    :return:
    """
    second_s = 1
    minute_s = 60 * second_s
    hour_s = 60 * minute_s
    day_s = 24 * hour_s

    if today_time:
        now = today_time
    else:
        now = datetime.datetime.now()
    now_time_stamp = time.mktime(now.timetuple())
    un_time = now_time_stamp - day * day_s - hour * hour_s - minute * minute_s - second * second_s
    return datetime.datetime.fromtimestamp(un_time)


if __name__ == '__main__':
    print(get_before_date(11, datetime.date(2000, 12, 12)))
    print(get_before_datetime(11, datetime.datetime(2000, 12, 12, 12, 12, 12)))
    print(get_before_time(day=11, hour=3))
    a = datetime.datetime.now()
    print(a.year)
    print(a.month)
    print(a.day)