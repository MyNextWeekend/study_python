# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 21:50
# @Author  : hejinhu
import csv
import os


def file_name(file_path):
    '''返回路径下的文件'''
    list = []
    names = os.listdir(file_path)
    for i in names:
        path = os.path.join(file_path, i)
        if os.path.isfile(path):
            list.append(path)
    return list


def write_csv(list):
    with open('a.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(list)


if __name__ == '__main__':
    list = file_name('./')
    write_csv(list)
