# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 11:33
# @Author  : hejinhu
import asyncio
import datetime


def current_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


async def do_something():
    print(f'func do_some_thing start: {current_time()}')
    await asyncio.sleep(3)
    print(f'func do_some_thing end: {current_time()}')


def run():
    """异步协程操作"""
    task_list = [do_something(), do_something()]
    print(f'func run start: {current_time()}')
    asyncio.run(asyncio.wait(task_list))
    print(f'func run end: {current_time()}')


if __name__ == '__main__':
    run()
    print("main done...")
