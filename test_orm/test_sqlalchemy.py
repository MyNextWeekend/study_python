# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 10:25
# @Author  : hejinhu
import time

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@106.55.186.222:3306/study?charset=utf8",
                       echo=True,  # 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
                       pool_size=8,  # 连接池的大小，默认为5个，设置为0时表示连接无限制
                       pool_recycle=60 * 30  # 设置时间以限制数据库多久没连接自动断开
                       )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    password = Column(String(64))
    address = Column(String(64))
    age = Column(Integer)
    birthday = Column(Date)
    six = Column(String(64))

    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email
    def __repr__(self):
        return f'id:{self.id},name:{self.name},password:{self.password},'

    def to_dic(self):
        return {
            "name": self.name,
            "password": self.password,
            "address": self.address,
            "age": self.age,
            "birthday": self.birthday,
            "six": self.six
        }


from sqlalchemy.orm import sessionmaker

# 创建session
DbSession = sessionmaker(bind=engine)
session = DbSession()
"""
批量插入共有以下几种方法，对它们的批量做了比较，分别是：
session.add_all() < bulk_save_object() < bulk_insert_mappings() < SQLAlchemy_core()
"""

# 增
# p = People()
# p.name = '谢海珊'
# p.six = '女'
# p.age = 18
# p.address = '湖北随州'
# p.birthday = '1998-05-20'
# session.add(p)
# session.commit()
from faker import Faker

f = Faker(locale='zh-CN')
# 批量增加-->bulk_save_object()
# objs = []
# for i in range(10000):
#     p = People()
#     p.name = f.name()
#     p.six = f.name()
#     p.age = f.pyint(min_value=0, max_value=9999, step=1)
#     p.address = f.address()
#     p.birthday = f.date(pattern="%Y-%m-%d", end_datetime=None)
#     objs.append(p)
# start = time.time()
# session.bulk_save_objects(objs)
# session.commit()
# print(time.time() - start)  # 30s

# 批量增加-->bulk_insert_mappings()
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
session.bulk_insert_mappings(People, objs)
session.commit()
print(time.time() - start)  # 30s

# 批量增加-->
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
session.execute(
    # People.__table__.insert().values(objs)  # 3.101
    People.__table__.insert(), objs  # 2.766
)
session.commit()
print(time.time() - start)

# 查询
# a = session.query(People).filter(People.name == '谢海珊').all()
# print(a)
