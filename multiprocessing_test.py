# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 21:56
# @Author  : hejinhu
import os
from multiprocessing import Pool
import time
import random


def aa(num):
    time.sleep(random.randint(1, 9))
    print(f'线程【{os.getpid()}】输出了【{num}】')
    return num * num


def suss(msg):
    print(f'线程【{os.getpid()}】拿到了【{msg}】')


def err(msg):
    print(f'线程【{os.getpid()}】输出异常：【{msg}】')


def mul():
    """多进程操作"""
    p = Pool(2)
    for i in range(3):
        p.apply_async(func=aa, args=(i,), error_callback=err, callback=suss)
    p.close()
    p.join()


if __name__ == '__main__':
    mul()
