# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 23:44
# @Author  : MyNextWeekend
import cv2
import numpy as np


def show(image):
    cv2.imshow("box", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blur(image):
    """均值滤波
    简单的平均卷积操作
    """
    blur = cv2.blur(image, (3, 3))
    return blur


def box_filter(image):
    """方框滤波
    基本和均值一样，可以选择归一化
    """
    box = cv2.boxFilter(image, -1, (3, 3), normalize=True)
    # box = cv2.boxFilter(img, -1, (3, 3), normalize=False)
    return box


def gaussian_blur(image):
    """高斯滤波
    高斯模糊的卷积核里的数值是满足高斯分布的，相当于更加重视中间的值
    """
    gaussian = cv2.GaussianBlur(image, (5, 5), 1)
    return gaussian


def median_blur(image):
    """中指滤波
    相当于从小到大排序，取中间的值
    """
    median = cv2.medianBlur(image, 5)
    return median


def all_pictures(*args):
    """将传入的多个图片横向拼接"""
    res = np.hstack(args)
    return res


if __name__ == '__main__':
    img = cv2.imread("./pictures/04_LenaNoise.png")
    blur = blur(img)
    box = box_filter(img)
    gaussian = gaussian_blur(img)
    median = median_blur(img)
    img = all_pictures(blur, box, gaussian, median)
    show(img)
