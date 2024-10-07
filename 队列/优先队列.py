# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 11:24
# @Author  : MyNextWeekend

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        # self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item))
        # heapq.heappush(self._queue, (priority, self._index, item))
        # self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)


if __name__ == '__main__':
    pri_queue = PriorityQueue()
    pri_queue.push("a", 4)
    pri_queue.push("w", 3)
    pri_queue.push("e", 5)
    pri_queue.push("r", 6)
    pri_queue.push("t", 1)
    for i in range(5):
        print(pri_queue.pop())
