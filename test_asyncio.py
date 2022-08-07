# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 11:33
# @Author  : hejinhu
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


async def do_something():
    print('方法开始')
    await asyncio.sleep(20)
    print('方法结束')


def do():
    """异步操作"""
    task_list = [do_something(), do_something()]
    print('------')
    asyncio.run(asyncio.wait(task_list))
    print('done')


def do_thread():
    """多线程操作"""
    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for i in range(5):
            res = t.submit(do_something)
            obj_list.append(res)

        for i in as_completed(obj_list):
            response = i.result()


def do_process():
    """多进程操作"""
    with ProcessPoolExecutor(max_workers=5) as p:
        obj_list = []
        for i in range(5):
            res = p.submit(do_something)
            obj_list.append(res)

        for i in as_completed(obj_list):
            response = i.result()


if __name__ == '__main__':
    do()
    print(123)
