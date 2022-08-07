# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 21:58
# @Author  : hejinhu
import logging
import datetime
import os


def logger(name=__name__):
    # 1- 日志的名称：  路径+名字(进程/日期)+后缀名
    dir = './logs/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    # 1- 日志的名称：  路径+名字(进程/日期)+后缀名
    logname = f"{dir}{datetime.datetime.now().strftime('%Y%m%d%H%M')}.log"
    # 2- 创建日志对象
    loggerObject = logging.getLogger(name)  #
    # 3- 日志级别
    loggerObject.setLevel(logging.INFO)
    # 4- 日志文件的属性
    rHandler = logging.FileHandler(logname, mode='a', encoding="utf-8")
    # 5- 日志内容的格式
    # 2021-01-20 17:29:44,688 INFO o.a.j.u.JMeterUtils: Setting Locale
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]: %(message)s ")
    rHandler.setFormatter(formatter)
    loggerObject.addHandler(rHandler)
    return loggerObject  # 返回日志对象


if __name__ == '__main__':
    lo = logger(__name__)
    lo.info(123)
