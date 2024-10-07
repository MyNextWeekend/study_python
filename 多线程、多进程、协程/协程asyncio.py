# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 11:33
# @Author  : MyNextWeekend
import asyncio
import datetime
import threading


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


def run_coroutine_in_thread():
    """在线程中运行协程"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # return_exceptions 将异常作为返回值，避免影响其他coroutine的运行
    futures = asyncio.gather(do_something(), do_something(), do_something(), return_exceptions=True)
    loop.run_until_complete(futures)
    loop.close()


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def set_task(self, task):
        self.tasks.append(task)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # return_exceptions 将异常作为返回值，避免影响其他coroutine的运行
        futures = asyncio.gather(*self.tasks, return_exceptions=True)
        loop.run_until_complete(futures)
        loop.close()


if __name__ == '__main__':
    # run()  # 方式一：直接启动协程处理

    # t = threading.Thread(target=run_coroutine_in_thread)  # 方式二：创建线程并运行协程
    # t.start()
    # t.join()

    t = MyThread()  # 方式三：自定义类继承Thread，启用协程任务
    t.set_task(do_something())
    t.set_task(do_something())
    t.set_task(do_something())
    t.start()
    t.join()
    print("main done...")
