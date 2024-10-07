# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 00:59
# @Author  : MyNextWeekend
import cv2
import numpy as np

img = cv2.imread("./pictures/05_Dige.png")

kernel = np.ones((5, 5), np.uint8)
# 开运算：先腐蚀再膨胀
open_pic = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel=kernel)

# 闭运算：先膨胀再腐蚀
close_pic = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=kernel)

# 梯度运算：膨胀之后的图形 减去 腐蚀之后的图形
gradient_pic = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel=kernel)

# 礼帽：原始输入的图形 减去 开运算之后的图形
tophat_pic = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel=kernel)

# 黑帽：闭运算之后的图形 减去 原始输入的图形
blackhat_pic = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel=kernel)

# 把所有图片横向拼接
all_pic = np.hstack((img, open_pic, close_pic, gradient_pic, tophat_pic, blackhat_pic))
cv2.imshow("tupian", all_pic)
cv2.waitKey(0)
