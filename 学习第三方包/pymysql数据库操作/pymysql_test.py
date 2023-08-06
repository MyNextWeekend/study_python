# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 10:47
# @Author  : hejinhu
import time

import pymysql


def run():
    conn = pymysql.Connect(host="106.55.186.222", port=3306,
                           user="study_python", password="7HwRmjpwTJdPacCb",
                           database="study_python")
    cursor = conn.cursor()
    conn.begin()  # 开启事物
    try:
        sql1 = "INSERT INTO student (name,age,gender) VALUES ('张三',18,'男');"
        result = cursor.execute(sql1)  # 执行sql
        print(result)  # 查看影响行数
        sql2 = "update student set age=29 where name='张三';"
        result = cursor.execute(sql2)
        print(result)
        sql3 = "update student set age=29 where name='张三11';"
        result = cursor.execute(sql3)
        print(result)
        conn.commit()  # 提交
    except Exception as e:
        conn.rollback()  # 回滚
        print(e)


if __name__ == '__main__':
    run()
