# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 23:29
# @Author  : hejinhu
class Singleton:
    def __new__(cls, *args, **kwargs):
        """设置成单例对象"""
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
