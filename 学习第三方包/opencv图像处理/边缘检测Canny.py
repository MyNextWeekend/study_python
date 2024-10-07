# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 12:14
# @Author  : MyNextWeekend
import cv2  # opencv的缩写为cv2
import numpy as np  # numpy数值计算工具包

"""
① Canny边缘检测流程：

   使用高斯滤波器，以平滑图像，滤除噪声。

   计算图像中每个像素点的梯度强度和方向。

   应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。

   应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。

   通过抑制孤立的弱边缘最终完成边缘检测。
"""

img = cv2.imread('pictures/05_Dige.png', cv2.IMREAD_GRAYSCALE)

v1 = cv2.Canny(img, 80, 150)  # 第二个参数为minVal，第三个参数为maxVal
v2 = cv2.Canny(img, 50, 100)

res = np.hstack((v1, v2))
cv2.imshow("aaa", res)
cv2.waitKey()
cv2.destroyAllWindows()
