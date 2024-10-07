# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 21:56
# @Author  : MyNextWeekend
import datetime
import os
import multiprocessing
import time
from concurrent.futures import as_completed, ProcessPoolExecutor


def current_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def do_some_thing(num):
    print(f'func do_some_thing start: {current_time()}【{os.getpid()}】get【{num}】')
    time.sleep(2)
    print(f'func do_some_thing end: {current_time()}【{os.getpid()}】')
    return num * num


def suss_call(msg):
    print(f'线程【{os.getpid()}】拿到了【{msg}】')


def err_call(msg):
    print(f'线程【{os.getpid()}】输出异常：【{msg}】')


def run():
    """多进程操作"""
    print("func run start")
    pool = multiprocessing.Pool(2)
    for i in range(3):
        pool.apply_async(func=do_some_thing, args=(i,), error_callback=err_call, callback=suss_call)
    pool.close()  # 先关闭池子
    pool.join()  # 然后才能等待任务完成
    print("func run end")


def run02():
    """多进程操作"""
    print("func run02 start")
    with ProcessPoolExecutor(max_workers=5) as p:
        obj_list = []
        for i in range(5):
            res = p.submit(do_some_thing, i)
            obj_list.append(res)

        for i in as_completed(obj_list):
            response = i.result()
    print("func run02 end")


if __name__ == '__main__':
    run()
    # run02()
    print("main done...")
