import time

import gevent
from gevent import monkey

# 猴子补丁，把一些同步方法替换为gevent实现的异步方法
monkey.patch_all()

"""
优点：gevent实现把第三方包的同步方法 修改为自己内部的异步方法
"""


def func_a():
    print("func_a start...")
    time.sleep(3)
    print("func_a end...")


def run():
    t1 = gevent.spawn(func_a)
    t2 = gevent.spawn(func_a)
    gevent.joinall([t1, t2])


if __name__ == "__main__":
    run()
