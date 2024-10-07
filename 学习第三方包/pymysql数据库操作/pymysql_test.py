# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 10:47
# @Author  : MyNextWeekend
import datetime
import random
import time

import pymysql


class MysqlUtil:
    def __init__(self):
        self.conn = pymysql.Connect(host="106.55.186.222", port=3306,
                                    user="study_python", password="nTMX8sPDSrsHzLC7",
                                    database="study_python")
        self.cursor = self.conn.cursor()

    def insert_many(self, sql, insert_args=None):
        try:
            result = self.cursor.executemany(sql, insert_args)
            self.conn.commit()
            return result
        except Exception as e:
            print(e)
            self.conn.rollback()

    def query_sql(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()


if __name__ == '__main__':
    # mysql = MysqlUtil()
    # res = mysql.query_sql("select * from student")
    # print(res)
    mysql = MysqlUtil()
    today = datetime.datetime.now()
    for i in range(30):
        insert_arg = []
        insert_sql = "insert student (name,call_id,start_time,end_time,create_date) value (%s,%s,%s,%s,%s)"
        create_date = today - datetime.timedelta(days=i)
        for j in range(1000000):
            insert_arg.append(
                (random.choice(["111", "222", "333", "444"]), f"{i}-{j}", create_date, create_date, create_date)
            )
            if j % 10000 == 0:
                res = mysql.insert_many(insert_sql, insert_arg)
                print(f"进度：{i}--{j} 结果是：{res}")
                insert_arg = []

        res = mysql.insert_many(insert_sql, insert_arg)
        print(res)
