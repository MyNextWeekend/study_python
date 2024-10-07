# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 12:18
# @Author  : MyNextWeekend
import cv2  # opencv的缩写为cv2
import numpy as np  # numpy数值计算工具包

img = cv2.imread('pictures/20190618124505345.png')
# 1. 倍数缩放
res1 = cv2.resize(img, (0, 0), fx=3, fy=1)  # (0,0)表示不确定具体值，fx=3 相当于行像素 x 乘 3，fy=1 相当于 y 乘 1
# 2. 等比例缩放
res2 = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)  # 同比例放缩

cv2.imshow("pic", res2)
cv2.waitKey(0)
