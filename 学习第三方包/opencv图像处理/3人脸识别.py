# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 15:59
# @Author  : MyNextWeekend
import cv2
import os

# 生成LBPH识别器实例模型
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 使用之前训练好的模型
recognizer.read('trainer/trainer.yml')
names = ["张三", "222", "王五"]


def face_detect(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像转换成灰度
    # 人脸识别器
    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(img_gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)  # 红色方框
        cv2.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 0, 255), thickness=1)  # 红色圆形
        # 与库中数据匹配分数
        ids, confidence = recognizer.predict(img_gray[y:y + h, x:x + w])
        if confidence > 80:
            text = "unknow"
            cv2.putText(img, text, (x + 10, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color=(0, 255, 0), thickness=1)
        else:
            text = f"{names[ids - 1]}"
            cv2.putText(img, text, (x + 10, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color=(0, 255, 0), thickness=1)
    cv2.imshow("result", img)
    cv2.waitKey(1)


def get_name():
    pass


cap = cv2.VideoCapture(0)
get_name()
while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        break  # 取不到图像的时候就退出
    face_detect(frame)
    key = cv2.waitKey(1)  # 图像展示时间延时1ms，这个中间也在等待键盘输入
    if key == 27:  # esc键对应的ASCII码是27
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 销毁所有窗口
