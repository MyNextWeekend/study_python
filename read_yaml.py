# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 22:21
# @Author  : hejinhu
import yaml
import pymysql

with open('./data_file/config.yaml','r') as f:
    cfg = yaml.load(f)
data = cfg['mysql']['config']
print(data)

db = pymysql.connect(**data)
cursor = db.cursor()
cursor.execute('show tables;')
d = cursor.fetchall()
print(d)