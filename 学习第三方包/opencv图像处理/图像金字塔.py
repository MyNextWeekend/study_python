# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 12:22
# @Author  : MyNextWeekend
import cv2  # opencv的缩写为cv2
import numpy as np  # numpy数值计算工具包

"""
① 金字塔的底层是比较大，越往上越小，图像金字塔就是把图像组合成金字塔的形状。
② 图像金字塔可以做图像特征提取，做特征提取时有时可能不光对原始输入做特征提取，可能还会对好几层图像金字塔做特征提取。
   可能每一层特征提取的结果是不一样的，再把特征提取的结果总结在一起。
③ 常用的两种图像金字塔形式：
    高斯金字塔
    拉普拉斯金字塔
"""
img = cv2.imread('pictures/20190618124505345.png')

up = cv2.pyrUp(img)
up_down = cv2.pyrDown(up)  # 先上采样再下采样

all_pic = np.hstack((img, up_down))
cv2.imshow("aaa", all_pic)
cv2.waitKey(0)


"""
拉普拉斯金字塔
① 拉普拉斯金字塔的每一层图像尺寸不变。
② 拉普拉斯金字塔的每一层操作都是上一层处理后作为输入，该输入减去该输入缩小放大后的图像，获得该层的输出。
"""
img = cv2.imread('pictures/20190618124505345.png')
down = cv2.pyrDown(img)
down_up = cv2.pyrUp(down)
L_1 = img - down_up
cv2.imshow("aaa", L_1)
cv2.waitKey(0)
print(L_1.shape)
