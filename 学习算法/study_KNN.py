# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 22:16
# @Author  : MyNextWeekend
import numpy as np
import pandas as pd

data = pd.read_csv(r'a.csv', header=0)
# 显示前N行记录。默认的值为5
data.head()
# 显示末尾N行，默认的值为5
data.tail()
# 随机抽取样本，默认抽取一条，我们可以通过参数进行指定抽取样本的数量
data.sample(10)
# 将类别文本映射为数值类型
data['xxx'] = data['xxx'].map({'aa': 0, 'bb': 1})
# 删除不需要的id列
data.drop('id', axis=1, inplace=True)
# data.drop_duplicated().any()
# 查看数据集的数量
len(data)
# 删除重复的记录
data.drop_duplicates(inplace=True)
# 查看列中数据的种类的个数
data['aa'].value_counts()


class KMeans:
    """Kmeans聚类算法实现"""

    def __init__(self, k, times):
        """初始化
        k: int 聚成几个类
        times: int 迭代次数
        """
        self.k = k
        self.times = times

    def fit(self, X):
        """根据所给数据训练
        X: 类数组类型，形如：[样本数量，特征数量]
        """
        X = np.asarray(X)
        # 设置随机数种子，以便于可以相同的随机系列，以便随机结果重现
        np.random.seed(0)
        # 从数组中随机选择K个点作为初始聚类中心
        self.cluster_centers_ = X[np.random.randint(0, len(X), self.k)]
        # 用于存放数据所属标签
        self.labels_ = np.zeros(len(X))
        # 开始迭代
        for t in range(self.times):
            # 循环遍历样本计算每个样本与聚类中心的距离
            for index, x in enumerate(X):
                # 计算每个样本与每个聚类中心的欧式距离
                dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2, axis=1))
                # 将最小距离的索引赋值给标签数组，索引的值就是当前所属的簇。范围威威（0，K-1）
                self.labels_[index] = dis.argmin()
            # 循环遍历每一个数更新聚类中心
            for i in range(self.k):
                # 计算每个簇内所有点的均值，用来更新聚类中心
                self.cluster_centers_[i] = np.mean(X[self.labels_ == i], axis=0)

    def predict(self, X):
        """预测样本属于哪个簇
        x: 类数组类型。形如[样本数量。特征数量]
        result: 类数组，每一个x所属的簇
        """
        X = np.asarray(X)
        result = np.zeros(len(X))
        for index, x in enumerate(X):
            # 计算样本与聚类中心的距离
            dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2, axis=1))
            # 找到距离最近的聚类中中心划分一个类别
            result[index] = dis.argmin()
        return result
