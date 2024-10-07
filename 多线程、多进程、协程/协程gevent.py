import datetime
import time
import gevent
from gevent import monkey

monkey.patch_all()  # 猴子修补 动态修改

"""
官网  http://www.gevent.org/api/gevent.html

注意：在任何时刻，只有一个协程在运行。
"""


def current_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def do_some_thing():
    print(f"func do_some_thing start: {current_time()}")
    time.sleep(2)  # 猴子补丁 自动修改为gevent.sleep()
    print(f"func do_some_thing end: {current_time()}")


def run():
    print("func run start...")
    gevent.spawn(do_some_thing)  # 启动一个协程任务并执行
    gevent.spawn(do_some_thing)
    time.sleep(3)  # 主线程结束会结束所有协程，因此休息
    print('func run end ....')


def run02():
    print("func run02 start...")
    job1 = gevent.spawn(do_some_thing)  # 启动一个协程任务并执行
    job2 = gevent.spawn(do_some_thing)
    gevent.joinall([job1, job2])  # 主动等待指定任务 执行完成
    print('func run02 end ....')


if __name__ == '__main__':
    # run()
    run02()
    print("main done...")
