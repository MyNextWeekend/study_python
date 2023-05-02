# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 01:27
# @Author  : hejinhu

import cv2
import numpy as np

img = cv2.imread("./pictures/06_pie.png")

# 计算x轴方向的梯度差值（CV_64F可以保存负数）
sobel_x_pic = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_x_pic = cv2.convertScaleAbs(sobel_x_pic)

# 计算y轴方向的梯度差值（CV_64F可以保存负数）
sobel_y_pic = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_y_pic = cv2.convertScaleAbs(sobel_y_pic)

# 将x轴和y轴的图像按照权重进行相加
sobel_xy_pic = cv2.addWeighted(sobel_x_pic, 0.5, sobel_y_pic, 0.5, 0)

# 把所有图片横向拼接
all_pic = np.hstack((img, sobel_x_pic, sobel_y_pic, sobel_xy_pic))
cv2.imshow("tupian", all_pic)
cv2.waitKey(0)
