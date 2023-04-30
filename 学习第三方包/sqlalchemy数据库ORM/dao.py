# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 15:17
# @Author  : hejinhu
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
