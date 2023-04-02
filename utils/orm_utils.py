# -*- coding: utf-8 -*-
# @Time    : 2023/4/2 14:45
# @Author  : hejinhu
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class ORM:
    def __init__(self):
        engine = create_engine("mysql+pymysql://root:123456@106.55.186.222:3306/study?charset=utf8",
                               echo=True,  # 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
                               pool_size=8,  # 连接池的大小，默认为5个，设置为0时表示连接无限制
                               pool_recycle=60 * 30  # 设置时间以限制数据库多久没连接自动断开
                               )
        # 创建session
        session_factory = sessionmaker(bind=engine)
        # session = scoped_session(session_factory=session_factory)
        self.session = session_factory()

    def get_session(self):
        return self.session


if __name__ == '__main__':
    s = ORM().get_session()
    s.add("some_obj")
    s.commit()