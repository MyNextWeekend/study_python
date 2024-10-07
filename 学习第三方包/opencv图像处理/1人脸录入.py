# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 14:45
# @Author  : MyNextWeekend
import random

import cv2

# 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
cap = cv2.VideoCapture(0)

while cap.isOpened():  # 判断视频或者摄像头是否成功打开
    flag, frame = cap.read()  # 按帧读取视频
    if not flag:
        break  # 取不到图像的时候就退出

    cv2.imshow("t", frame)  # 在界面展示图片
    key = cv2.waitKey(1)  # 图像展示时间延时1ms，这个中间也在等待键盘输入
    if key == 27:  # esc键对应的ASCII码是27
        break
    if key == ord("s"):
        name = input("请输入名称：")
        cv2.imwrite(f"./trainer/{name}.jpg", frame)
        print(f"success save {name}.jpg")

cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 销毁所有窗口
