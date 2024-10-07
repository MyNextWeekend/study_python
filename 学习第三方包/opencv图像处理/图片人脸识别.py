# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 13:14
# @Author  : MyNextWeekend
import cv2

# 加载待处理图片
img = cv2.imread("pictures/20190618124505345.png")
# 加载人脸特征（特征下载位置https://github.com/opencv/opencv   目录：data/haarcascades）
# face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
# 找到符合特征的所有坐标位置
faces = face_detector.detectMultiScale(img)
# 遍历所有符合的坐标
for x, y, w, h in faces:
    # 在坐标位置画一个红色的矩形
    cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255])
# 将处理之后的图片展示
cv2.imshow("识别后结果", img)
# 设置展示时间
cv2.waitKey(0)
# 销毁所有的窗口
cv2.destroyAllWindows()
