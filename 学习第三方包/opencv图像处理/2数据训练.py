# -*- coding: utf-8 -*-
# @Time    : 2023/5/14 15:17
# @Author  : MyNextWeekend
import os

import cv2
from PIL import Image
import numpy as np


def get_image_and_labels(path):
    result_face_samples = []  # 存储人脸数据
    result_names = []  # 存储姓名数据
    # 人脸识别器
    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    # 将路径下所有的图片位置拿到
    image_paths = [os.path.join(path, i) for i in os.listdir(path)]
    for image_path in image_paths:
        # 对非jpg的文件跳过处理
        if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
            continue
        # 打开图片，灰度化   PIL有九种模式：1、L、P、RGB、RGBA、CMYK、YCbCr、I、F
        pil_image = Image.open(image_path).convert("L")
        # 图像转换为numpy
        numpy_image = np.array(pil_image)
        # numpy_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 图像转换成灰度
        # 获取人脸特征
        image_faces = face_detector.detectMultiScale(numpy_image)
        # 这张图对应的名字， 这里必须取数字否则训练的时候报错
        name = int(os.path.split(image_path)[1].split(".")[0])
        for x, y, w, h in image_faces:
            result_names.append(name)
            result_face_samples.append(numpy_image[y:y + h, x:x + w])
            # cv2.imshow("show", img_gray[y:y + h, x:x + w])
            # cv2.waitKey(0)
    return result_face_samples, result_names


if __name__ == '__main__':
    images_path = "./trainer/"
    faces, names = get_image_and_labels(images_path)
    # 生成LBPH识别器实例模型  OpenCV提供了三种人脸识别的方法，分别是LBPH方法、EigenFishfaces方法、Fisherfaces方法。
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 训练。对每个参考图像计算LBPH，得到一个向量，每个人脸都是整个向量集中的一个点
    recognizer.train(faces, np.array(names))
    recognizer.save('./trainer/trainer.yml')
