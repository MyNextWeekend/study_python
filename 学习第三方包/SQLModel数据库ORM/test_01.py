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
        result = session.exec(sql)
        for row in result:
            print(row)
