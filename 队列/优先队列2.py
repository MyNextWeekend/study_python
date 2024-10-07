# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 11:38
# @Author  : MyNextWeekend
import queue

pri_queue = queue.PriorityQueue()
pri_queue.put((5, "w"))
pri_queue.put((7, "q"))
pri_queue.put((4, "e"))
pri_queue.put((5, "r"))
pri_queue.put((1, "t"))
print(pri_queue.queue)
while not pri_queue.empty():
    print(pri_queue.get())
