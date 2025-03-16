import functools


def singleton(cls):
    """
    将一个类作为单例
    来自 https://wiki.python.org/moin/PythonDecoratorLibrary#Singleton
    """

    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kw):
        it = cls.__dict__.get('__it__')
        if it is not None:
            return it

        cls.__it__ = it = cls.__new_original__(cls)
        it.__init_original__(*args, **kw)
        return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__

    return cls


# def singleton(cls):
#     """
#     将一个类作为单例
#     """
#     # 缓存实例
#     instances = {}
#
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             # 创建类的实例并缓存
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper