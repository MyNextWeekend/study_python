# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 00:48
# @Author  : MyNextWeekend
import cv2
import numpy as np

img = cv2.imread("./pictures/05_Dige.png")

kernel = np.ones((5, 5), np.uint8)
# 腐蚀操作通常是拿二值图像做腐蚀操作
erode_pic = cv2.erode(img, kernel=kernel, iterations=1)  # iterations操作次数
# 膨胀操作通常是拿二值图像做腐蚀操作
dilate_pic = cv2.dilate(img, kernel=kernel, iterations=1)

# 把所有图片横向拼接
all_pic = np.hstack((img, erode_pic, dilate_pic))
cv2.imshow("tupian", all_pic)
cv2.waitKey(0)
