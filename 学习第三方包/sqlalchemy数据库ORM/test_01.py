# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 10:25
# @Author  : hejinhu
import asyncio
import threading
import time

from sqlalchemy import select
from orm_utils import db_orm
from dao import Student
from faker import Faker

fake = Faker(locale='zh-CN')


def split_list(obj_list: list, chunk_size: int):
    for i in range(0, len(obj_list), chunk_size):
        yield obj_list[i:i + chunk_size]


def add():
    """新增一个"""
    stu = Student(name="张三", age=18, gender="难")
    stu.gender = "什么鬼"
    session = db_orm.get_session()
    session.add(stu)
    session.commit()


def add_by_bulk_save_object(objs):
    """批量增加-->bulk_save_object()"""
    session = db_orm.get_session()
    session.bulk_save_objects(objs)  # 0.5s/1000条
    # session.add_all(objs)  # 13s/1000条
    session.commit()


def find_all():
    """查询"""
    session = db_orm.get_session()
    sql = select(Student).where(Student.name.in_(["李伟", "钟成"]))
    for i in session.scalars(sql):
        print(i.name)


async def async_insert_many(objs):
    """异步批量新增"""
    task = []
    for chunk in split_list(objs, 1000):
        task.append(asyncio.create_task(db_orm.insert_objects(chunk)))

    await asyncio.wait(task)  # 17s/10000条


def insert_by_thead(objs):
    ts = []
    for i in split_list(objs, 1000):
        ts.append(threading.Thread(add_by_bulk_save_object(i)))
    for i in ts:
        i.start()


def creat_student(num: int) -> list:
    res = []
    for i in range(num):
        stu = Student()
        stu.name = fake.name()
        stu.age = fake.random_int()
        stu.gender = fake.address()
        res.append(stu)
    return res


if __name__ == '__main__':
    start = time.time()

    find_all()

    # insert_by_thead(creat_student(10000))  # 2.0

    # add_by_bulk_save_object(creat_student(10000))  # 1.69

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(
    #     async_insert_many(creat_student(10000))  # 16.69
    # )

    print(f"花费时间是：{time.time() - start}s")
