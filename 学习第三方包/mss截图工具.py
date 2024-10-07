# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 17:08
# @Author  : MyNextWeekend
import mss
import numpy as np
import cv2

sct = mss.mss()
box = {"top": 50, "left": 50, "width": 200, "height": 200}

cv2.namedWindow("aaa", cv2.WINDOW_KEEPRATIO)  # 指定窗口类型
cv2.resizeWindow("aaa", 1920, 1080)
while True:
    if not cv2.getWindowProperty("aaa", cv2.WND_PROP_VISIBLE):
        cv2.destroyAllWindows()
        exit("程序结束。。。")
        break
    img = sct.grab(box)  # 按照指定位置截图
    img = np.array(img)  # 将截图转换为numpy数组
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 颜色处理（根据需求处理）
    cv2.imshow("aaa", img)  # 将截图在窗口进行展示
    cv2.waitKey(1)
