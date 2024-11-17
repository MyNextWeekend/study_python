import datetime

from sqlmodel import SQLModel, Field, select, Session
from orm_utils import engine


class Student(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=True)
    call_id: str = Field(nullable=True)
    start_time: datetime.datetime = Field(nullable=True)
    end_time: datetime.datetime = Field(nullable=True)
    create_date: datetime.datetime = Field(nullable=True)


if __name__ == '__main__':
    with Session(engine) as session:
        sql = select(Student).where(Student.id > 9999).limit(20)
        # 批量查询
        students = session.exec(sql)
        for stu in students:
            # 删除
            if stu.id == 593711:
                session.delete(stu)
                session.commit()
            # 修改
            if stu.name == "0-1":
                stu.name = "李四"
                session.commit()
            print(stu)
        # 新增
        user = Student(
            name="张三",
            call_id="123456",
            start_time=datetime.datetime.now(),
            end_time=datetime.datetime.now(),
            create_date=datetime.datetime.now(),
        )
        session.add(user)
        session.commit()
