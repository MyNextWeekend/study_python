# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 15:17
# @Author  : MyNextWeekend
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    """基类"""
    pass


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
