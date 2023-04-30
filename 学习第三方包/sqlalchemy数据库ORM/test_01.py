# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 10:25
# @Author  : hejinhu
import time

from 学习第三方包.sqlalchemy数据库ORM.dao import People
from 学习第三方包.sqlalchemy数据库ORM.properties import session_factory


def add():
    """新增一个"""
    p = People()
    p.name = '张三'
    p.six = '女'
    p.age = 18
    p.address = '湖北'
    p.birthday = '1998-05-20'
    session = session_factory()
    session.add(p)
    session.commit()


from faker import Faker

f = Faker(locale='zh-CN')

"""
批量插入共有以下几种方法，对它们的批量做了比较，分别是：
session.add_all() < bulk_save_object() < bulk_insert_mappings() < SQLAlchemy_core()
"""


def add_by_bulk_save_object():
    """批量增加-->bulk_save_object()"""
    objs = []
    for i in range(10000):
        p = People()
        p.name = f.name()
        p.six = f.name()
        p.age = f.pyint(min_value=0, max_value=9999, step=1)
        p.address = f.address()
        p.birthday = f.date(pattern="%Y-%m-%d", end_datetime=None)
        objs.append(p)
    start = time.time()
    session = session_factory()
    session.bulk_save_objects(objs)
    session.commit()
    print(time.time() - start)  # 30s


def add_by_bulk_insert_mappings():
    """批量增加-->bulk_insert_mappings()"""
    objs = []
    for i in range(100000):
        p = People()
        p.name = f.name()
        p.six = f.name()
        p.age = f.pyint(min_value=0, max_value=9999, step=1)
        p.address = f.address()
        p.birthday = f.date(pattern="%Y-%m-%d", end_datetime=None)
        a = vars(p)
        a.pop('_sa_instance_state', None)
        objs.append(a)
    start = time.time()
    session = session_factory()
    session.bulk_insert_mappings(People, objs)
    session.commit()
    print(time.time() - start)  # 30s


def add_by():
    """批量增加-->__table__.insert()"""
    objs = []
    for i in range(10000):
        p = People()
        p.name = f.name()
        p.six = f.name()
        p.age = f.pyint(min_value=0, max_value=9999, step=1)
        p.address = f.address()
        p.birthday = f.date(pattern="%Y-%m-%d", end_datetime=None)
        a = vars(p)
        a.pop('_sa_instance_state', None)
        objs.append(a)
    start = time.time()
    session = session_factory()
    session.execute(
        # People.__table__.insert().values(objs)  # 3.101
        People.__table__.insert(), objs  # 2.766
    )
    session.commit()
    print(time.time() - start)


def select():
    """查询"""
    session = session_factory()
    a = session.query(People).filter(People.name == 'zhangsan').all()
    print(a)
