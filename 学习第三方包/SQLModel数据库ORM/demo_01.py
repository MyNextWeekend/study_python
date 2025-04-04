import datetime

from sqlmodel import Field, SQLModel, select
from sqlmodel_utils import DBEnum, SQLModelUtil


class Student(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=True)
    call_id: str = Field(nullable=True)
    start_time: datetime.datetime = Field(nullable=True)
    end_time: datetime.datetime = Field(nullable=True)
    create_date: datetime.datetime = Field(nullable=True)


if __name__ == "__main__":
    db = SQLModelUtil(DBEnum.UAT, "fms")

    statement = select(Student).where(Student.id > 9999).limit(20)
    # 批量查询
    students = db.query_all(statement)
    for stu in students:
        # 删除
        if stu.id == 593711:
            db.delete(stu)
        # 修改
        if stu.name == "0-1":
            stu.name = "李四"
            db.update(stu)
        print(stu)
    # 新增
    user = Student(
        name="张三",
        call_id="123456",
        start_time=datetime.datetime.now(),
        end_time=datetime.datetime.now(),
        create_date=datetime.datetime.now(),
    )
    db.add(user)
