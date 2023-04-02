import datetime
import time


def get_before_day(date_str: str, day: int):
    """
    获取前几天日期
    :param date_str:日期字符串 格式：%Y-%m-%d %H:%M:%S 或者 %Y-%m-%d
    :param day:往前推的天数
    :return:日期字符串
    """
    try:
        date_str = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        date_str = time.strptime(date_str, '%Y-%m-%d')
    t = time.mktime(date_str)
    t = t - 24 * 60 * 60 * day
    date = time.strftime('%Y-%m-%d', time.localtime(t))
    date2 = time.strftime('%Y%m%d', time.localtime(t))
    return date, date2


if __name__ == '__main__':
    print(get_before_day("2022-1-2", 1))
