# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 16:26
# @Author  : hejinhu
import threading
import queue


class aa(threading.Thread):
    def __init__(self, aaaa:queue):
        super().__init__()
        self.a_list = aaaa

    def run(self) -> None:
        while not self.a_list.empty():
            print(self.a_list.get())


if __name__ == '__main__':
    aaaa = queue.Queue()
    aaaa.put(1)
    aaaa.put(2)
    aaaa.put(3)
    aaaa.put(4)
    aaaa.put(5)
    a_list = []
    for i in range(3):
        a = aa(aaaa)
        a.start()
        a_list.append(a)
    for i in a_list:
        i.join()
