# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 00:26
# @Author  : MyNextWeekend
import cv2
import numpy as np

img = cv2.imread("./pictures/qi.png")

# 超过阈值部分取maxval（最大值），否则取0
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# THRESH_BINARY的反转
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 大于阈值的部分设置为阈值，否则不变
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# 大于阈值的部分设置为阈值，否则设置为0
ret4, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# THRESH_TOZERO的反s转
ret5, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# 把所有图片横向拼接
all_pic = np.hstack((img, thresh1, thresh2, thresh3, thresh4, thresh5))
cv2.imshow("tupian", all_pic)
cv2.waitKey(0)
