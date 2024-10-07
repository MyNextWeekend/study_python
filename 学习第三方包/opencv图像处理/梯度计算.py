# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 01:27
# @Author  : MyNextWeekend

import cv2
import numpy as np

img = cv2.imread("./pictures/06_pie.png")

# --------------------------------------------------
# 不同算子质检的差异

# ① Sobel算子函数：cv2.Sobel(src, ddepth, dx, dy, ksize)，返回值为Sobel算子处理后的图像。
# ② 靠近最近点的左右和上下的权重最高，所以为±2。
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # 计算x轴方向的梯度差值（CV_64F可以保存负数）
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # 计算y轴方向的梯度差值（CV_64F可以保存负数）
sobel_x = cv2.convertScaleAbs(sobel_x)  # 取绝对值
sobel_y = cv2.convertScaleAbs(sobel_y)  # 取绝对值
sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)  # 将x轴和y轴的图像按照权重进行相加

#  Scharr算子对结果的差异更敏感一些。
scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr_x = cv2.convertScaleAbs(scharr_x)
scharr_y = cv2.convertScaleAbs(scharr_y)
scharr_xy = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

# ① Laplacian算子用的是二阶导，对噪音点更敏感一些。
# ② 如果中心点是边界，它与周围像素点差异的幅度会较大，Laplacian算子根据此特点可以把边界识别出来。
laplacian = cv2.Laplacian(img, cv2.CV_64F)  # 没有 x、y，因为是求周围点的比较
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((img, sobel_xy, scharr_xy, laplacian))  # 把所有图片横向拼接
cv2.imshow("tupian", res)
cv2.waitKey(0)
