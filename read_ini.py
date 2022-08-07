# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 22:09
# @Author  : hejinhu
from configparser import ConfigParser

file_path = './data_file/config.ini'
cfg = ConfigParser()
cfg.read(file_path)
list = cfg.items('mysql')
dic = dict(list)
print(dic)