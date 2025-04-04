# @Time    : 2023/4/30 15:19
# @Author  : MyNextWeekend
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker


class ORM:
    def __init__(self):
        # 同步连接
        db_url = "mysql+pymysql://study_python:7HwRmjpwTJdPacCb@106.55.186.222:3306/study_python?charset=utf8"
        engine = create_engine(db_url, echo=False, pool_size=8, pool_recycle=60 * 30)
        self.session_marker = sessionmaker(engine)

        # 异步连接
        async_url = "mysql+aiomysql://study_python:7HwRmjpwTJdPacCb@106.55.186.222:3306/study_python?charset=utf8"
        async_engine = create_async_engine(async_url, echo=False, pool_recycle=60 * 30)
        self.async_session = async_sessionmaker(async_engine)

    def get_session(self):
        """返回一个同步session"""
        return self.session_marker()

    async def insert_objects(self, objs):
        """异步存入数据库"""
        async with self.async_session() as session:
            try:
                async with session.begin():
                    session.add_all(objs)
            except Exception as e:
                # session.rollback()
                print(f"insert obj err: {e}")


db_orm = ORM()
