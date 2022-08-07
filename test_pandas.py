# -*- coding: utf-8 -*-
# @Time    : 2022/6/4 12:07
# @Author  : hejinhu
import pandas as pd
import numpy as np

# ---------------二维数据结构-----------
# 二维ndarray创建
data = np.zeros((5,),dtype=[('a','i4'),('b','f4'),('c','a10')])
data[:2] = [(1,2.,'hello'),(2,3.,'word')]
s = pd.DataFrame(data,index=['one','two','three','f','fivr'],columns=['c','a','b'])
# 嵌套列表
# s = pd.DataFrame([[1, 2, 3, 4], [6, 7, 8, 9]], index=['tt', 'yy'], columns=['a', 's', 'd', 'f'])

# 字典
# s = pd.DataFrame({'two': [1, 2, 3, 4], 'one': [2, 3, 4, 7]})
print(s)

# --------------一维数据结构-------------
# l = [1, 2, 3, 4, 5]
# li = np.random.randint(1, 10, 5)
# p = pd.Series(li, index=['a', 'b', 'c', 'd', 'e'])
# 没有值使用Nan补充
# p = pd.Series({'a': 555, 'e': 777}, index=['a', 'b', 'c', 'd', 'e'])
# 都适用相同的值
# p = pd.Series(3, index=['a', 'b', 'c', 'd', 'e'])
# 报错
# p = pd.Series([1,2,3,4,5], index=['a', 'b'])
# print(p)
