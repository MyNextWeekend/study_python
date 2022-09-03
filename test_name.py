# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 10:54
# @Author  : hejinhu
class ORM:
    def save(self):
        name = self.__class__.__name__
        print(name)
        dic = self.__dict__
        print(dic)
class User(ORM):
    height = 77
    def __init__(self,age):
        self.name = 'zhangsan'
        self.age = age
        print(self.__dict__)

if __name__ == '__main__':
    u = User(99)
    u.save()
