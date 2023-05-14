# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 15:59
# @Author  : hejinhu
import cv2
import os

# 生成LBPH识别器实例模型
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 使用之前训练好的模型
recognizer.read('trainner/trainner.yml')
names = []


def face_detect(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像转换成灰度
    # 人脸识别器
    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(img_gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv2.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 0, 255), thickness=1)
        # 与库中数据匹配分数
        ids, confidence = recognizer.predict(img_gray[y:y + h, x:x + w])
        if confidence > 80:
            cv2.putText(img, "未知", (x + 10, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color=(0, 255, 0), thickness=1)
        else:
            cv2.putText(img, f"{names[ids - 1]}", (x + 10, y - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, color=(0, 255, 0), thickness=1)
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

cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 销毁所有窗口
