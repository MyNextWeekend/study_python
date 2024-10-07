# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 16:19
# @Author  : MyNextWeekend
import cv2


def net_video():
    # 位置https://www.cnblogs.com/kiter/p/14599472.html
    cap = cv2.VideoCapture("rtmp://58.200.131.2:1935/livetv/dyjctv")
    while cap.isOpened():
        flag, frame = cap.read()
        cv2.imshow("hello", frame)
        cv2.waitKey(1)


if __name__ == '__main__':
    net_video()
