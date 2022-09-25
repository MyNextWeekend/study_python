# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 23:13
# @Author  : hejinhu
import queue
import threading
import time

# 多线程
# def test():
#     print('1')
#
#
# threading.Thread(target=test).start()

# 重写多线程
# class MyThread(threading.Thread):
#     def __init__(self, q: queue):
#         super().__init__()
#         self.q = q
#
#     def run(self) -> None:
#         while not self.q.empty():
#             print(f'线程{threading.currentThread()}消费了{self.q.get()}')
#
#
# # 生产者
# q = queue.Queue()
# for i in range(30):
#     q.put(i)
# f_list = []
# # 消费者
# for i in range(3):
#     m = MyThread(q)
#     m.start()
#     print(m)
#     f_list.append(m)
#     # m.join()
# for i in f_list:
#     i.join()


from concurrent.futures import ThreadPoolExecutor, wait


# 线程池
def test001():
    time.sleep(1)
    print(f'当前线程： {threading.currentThread().name}')


pool = ThreadPoolExecutor(10)
f_list = []
for _ in range(100000):
    f = pool.submit(test001)
    # f_list.append(f)
    # print('------------')
# print(len(f_list))
# wait(f_list)
print(f'zhu线程： {threading.currentThread().name}')
