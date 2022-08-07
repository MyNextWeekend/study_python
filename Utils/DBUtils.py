# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 14:05
# @Author  : hejinhu

import pymysql
from Config import DBConfig
from Utils.Singleton import Singleton


def outter(func):
    """数据库操作装饰器"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'数据库操作异常：{e}')

    return inner


class DBUtils(Singleton):
    def __init__(self):
        host = '127.0.0.1'
        port = 3306
        user = 'root'
        password = '123456'
        database = 'test'
        # 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                                        charset='utf8')
        except Exception as e:
            raise Exception(f'链接数据库异常:{e}')

    @outter
    def select_fetchall(self, sql):
        """查询全部数据"""
        # 得到一个可以执行SQL语句的光标对象
        with self.conn.cursor() as cursor:
            # 使用execute方法执行SQL语句
            cursor.execute(sql)
            res = cursor.fetchall()
        self.conn.commit()
        return res

    @outter
    def select_fetchone(self, sql):
        """查询一条数据"""
        # 得到一个可以执行SQL语句的光标对象
        with self.conn.cursor() as cursor:
            # 使用execute方法执行SQL语句
            cursor.execute(sql)
            res = cursor.fetchone()
        self.conn.commit()
        return res

    @outter
    def insert_sql(self, sql):
        """插入数据库"""
        with self.conn.cursor() as cursor:
            res = cursor.execute(sql)
        self.conn.commit()
        return res

    @outter
    def update_sql(self, sql):
        """更新数据库"""
        with self.conn.cursor() as cursor:
            res = cursor.execute(sql)
        self.conn.commit()
        return res

    def close(self):
        """关闭数据库连接"""
        self.conn.close()


db = DBUtils()
if __name__ == '__main__':
    list = db.select_fetchone('select * from test;')
    print(list)
