# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 09:34
# @Author  : MyNextWeekend
import random
from dataclasses import dataclass, field


@dataclass
class Param:
    index: int
    name: str = "张三"
    age: int = field(init=False)

    def __post_init__(self):
        self.age = random.randint(100, 200)


if __name__ == '__main__':
    p1 = Param(1, "aa")
    p2 = Param(2)
    p3 = Param(3)
    p4 = Param(4)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
