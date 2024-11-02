# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 10:47
# @Author  : MyNextWeekend
import datetime
import random

import pymysql

HOST = "106.55.186.222"
PORT = 3306
USER = "study_python"
PASSWORD = "nTMX8sPDSrsHzLC7"
DATABASE = "study_python"


class MySQLDatabase:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.user = USER
        self.password = PASSWORD
        self.database = DATABASE
        self.connection: pymysql.Connection | None = None

    def _connect(self):
        """连接到数据库"""
        if self.connection is None or not self.connection.open:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor  # 指示游标以字典的形式返回查询结果
            )

    def close(self):
        """关闭数据库连接"""
        if not self.connection:
            return
        if self.connection.open:
            self.connection.close()
        self.connection = None

    def query(self, sql: str, params=None) -> any:
        """执行查询并返回结果"""
        self._connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
        return result

    def execute(self, sql: str, params: tuple[any, ...] | None = None) -> int:
        """执行非查询操作（INSERT, UPDATE, DELETE），支持事务"""
        self._connect()
        result = 0
        try:
            with self.connection.cursor() as cursor:
                result = cursor.execute(sql, params)
            self.connection.commit()  # 提交事务
        except Exception as e:
            self.connection.rollback()  # 回滚事务
            print(f"execute sql err:{e}")  # 可以选择重新抛出异常或处理异常
        return result

    def executemany(self, sql: str, params_list: list[any]) -> int:
        """批量执行非查询操作（INSERT, UPDATE, DELETE），支持事务"""
        self._connect()
        result = 0
        try:
            with self.connection.cursor() as cursor:
                result = cursor.executemany(sql, params_list)
            self.connection.commit()  # 提交事务
        except Exception as e:
            self.connection.rollback()  # 回滚事务
            print(f"executemany sql error: {e}")  # 处理异常
        return result

    def __del__(self):
        self.close()


# 使用示例
if __name__ == "__main__":
    db = MySQLDatabase()

    # 执行查询
    results = db.query("SELECT * FROM student limit 10;")
    print(results)

    # 执行非查询
    db.execute("INSERT INTO student (name,call_id,start_time,end_time,create_date) VALUES (%s, %s, %s, %s, %s)",
               (
                   random.choice(["111", "222", "333", "444"]),
                   f"666",
                   datetime.datetime.now(),
                   datetime.datetime.now(),
                   datetime.datetime.now()
               ))
