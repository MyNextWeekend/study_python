# @Time    : 2022/9/4 10:25
# @Author  : MyNextWeekend
import asyncio
import threading
import time

from dao import Student
from faker import Faker
from orm_utils import db_orm
from sqlalchemy import select

fake = Faker(locale="zh-CN")


def split_list(obj_list: list, chunk_size: int):
    for i in range(0, len(obj_list), chunk_size):
        yield obj_list[i : i + chunk_size]


def creat_student():
    """构建一个学生对象"""
    stu = Student()
    stu.name = fake.name()
    stu.age = fake.random_int()
    stu.gender = fake.address()
    return stu


def build_many_students(num: int) -> list:
    """创建多个学生对象"""
    res = []
    for i in range(num):
        res.append(creat_student())
    return res


def find_all():
    """查询"""
    session = db_orm.get_session()
    sql = select(Student).where(Student.name.in_(["李伟", "钟成"]))
    for i in session.scalars(sql):
        print(i.name)


def add():
    """新增一个"""
    stu = creat_student
    session = db_orm.get_session()
    session.add(stu)
    session.commit()


def add_by_bulk_save_object(objs):
    """批量增加-->bulk_save_object()"""
    session = db_orm.get_session()
    session.bulk_save_objects(objs)  # 0.5s/1000条
    # session.add_all(objs)  # 13s/1000条
    session.commit()


async def async_insert_many(objs):
    """异步批量新增"""
    jobs = []
    for chunk in split_list(objs, 1000):  # 协程数量过多会导致数据库连接池爆
        jobs.append(asyncio.create_task(db_orm.insert_objects(chunk)))

    await asyncio.wait(jobs)  # 17s/10000条


def insert_by_thead(objs):
    """多线程写入"""
    jobs = []
    for chunk in split_list(objs, 1000):
        jobs.append(threading.Thread(add_by_bulk_save_object(chunk)))
    for job in jobs:
        job.start()


if __name__ == "__main__":
    start = time.time()

    find_all()

    # insert_by_thead(build_many_students(10000))  # 2.0

    # add_by_bulk_save_object(build_many_students(10000))  # 1.69

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(
    #     async_insert_many(build_many_students(10000))  # 16.69
    # )

    print(f"花费时间是：{time.time() - start}s")
