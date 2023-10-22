# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 11:33
# @Author  : hejinhu
import asyncio
import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


async def do_something():
    print(f'{current_time()} 方法开始')
    await asyncio.sleep(3)
    print(f'{current_time()} 方法结束')


def do_some():
    print(f'{current_time()} 方法开始')
    time.sleep(3)
    print(f'{current_time()} 方法结束')


def do():
    """异步协程操作"""
    task_list = [do_something(), do_something()]
    print(f'{current_time()} start')
    asyncio.run(asyncio.wait(task_list))
    print(f'{current_time()} done')


def do_thread():
    """多线程操作"""
    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for i in range(5):
            res = t.submit(do_some)
            obj_list.append(res)

        for i in as_completed(obj_list):
            response = i.result()


def do_process():
    """多进程操作"""
    with ProcessPoolExecutor(max_workers=5) as p:
        obj_list = []
        for i in range(5):
            res = p.submit(do_some)
            obj_list.append(res)

        for i in as_completed(obj_list):
            response = i.result()


if __name__ == '__main__':
    do()
    print("done")
