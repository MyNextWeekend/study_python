# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 23:13
# @Author  : MyNextWeekend
import datetime
import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


def current_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 线程池
def do_some_thing():
    print(f'func do_some_thing start: {current_time()} {threading.currentThread().name}')
    time.sleep(1)
    print(f'func do_some_thing end: {current_time()} {threading.currentThread().name}')


def run():
    print(f"func run start")
    pool = ThreadPoolExecutor(10)
    f_list = []
    for _ in range(10):
        f = pool.submit(do_some_thing)
        f_list.append(f)
    wait(f_list)
    print(f'func run end')


def run02():
    print("func run02 start")
    with ThreadPoolExecutor(max_workers=5) as pool:
        obj_list = []
        for i in range(5):
            res = pool.submit(do_some_thing)  # 向线程池提交任务
            obj_list.append(res)

        for i in as_completed(obj_list):  # 等待任务执行完成
            response = i.result()
    print("func run02 end")


if __name__ == '__main__':
    # run()
    run02()
    print("main done...")
