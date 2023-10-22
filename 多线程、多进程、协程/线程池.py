# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 23:13
# @Author  : hejinhu
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait


# 线程池
def test001():
    time.sleep(1)
    print(f'当前线程： {threading.currentThread().name}')


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    f_list = []
    for _ in range(10):
        f = pool.submit(test001)
        f_list.append(f)
    wait(f_list)
    print(f'主线程： {threading.currentThread().name}')
    print("done")
