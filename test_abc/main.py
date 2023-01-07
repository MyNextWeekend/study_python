# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 07:47
# @Author  : hejinhu
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    @abstractmethod
    def run(self) -> int:
        pass

    @abstractmethod
    def rrr(self):
        pass


class Apple(Base):
    def run(self):
        print(777)


if __name__ == '__main__':
    Apple().run()
