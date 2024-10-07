# -*- coding: utf-8 -*-
# @Time    : 2023/4/1 16:46
# @Author  : MyNextWeekend
import random
import time

"""
实现随机数有一定的规律
可以走通的是：
            0-->1
            1-->2,3
            3-->0,3
            3-->0
"""
tu = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0]
]


def play(index):
    print(f"当前播放动画：{index}")


if __name__ == '__main__':
    start = 0
    while True:
        x = random.randint(0, 3)
        while 0 == tu[start][x]:
            x = random.randint(0, 3)
        play(x)
        time.sleep(2)
        start = x
