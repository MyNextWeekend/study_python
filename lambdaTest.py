import time
import random


def outter(func):
    def inner(*args, **kwargs):
        start = time.time()
        # print('方法运行之前')
        res = func(*args, **kwargs)
        # print('后置输入')
        end = time.time()
        print('消耗时间：%d' % (end - start))
        return res

    return inner


@outter
def sum(a, b):
    return a + b


# print(sum(1, 2))


# def sunn():
#     def inner():
#         print('1111111')
#     return inner
#
#
# sunn()()
z = lambda x: x + 2
print(z(3))
