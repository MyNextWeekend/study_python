from enum import Enum

from sqlmodel import Session, SQLModel, create_engine, text


class DBEnum(str, Enum):
    SIT = ""
    UAT = "mysql+pymysql://study_python:nTMX8sPDSrsHzLC7@106.55.186.222:3306"


class SQLModelUtil:
    def __init__(self, db_config: DBEnum, database: str):
        db_url = f"{db_config}/{database}?charset=utf8"
        self.engine = create_engine(
            db_url, echo=True, pool_size=8, pool_recycle=60 * 30
        )

    def add(self, model: SQLModel):
        """
        新增数据
        :param model:
        :return:
        """
        with Session(self.engine) as session:
            session.add(model)
            session.commit()
            session.flush()
            return model

    def delete(self, model: SQLModel):
        """
        删除数据
        :param model:
        :return:
        """
        with Session(self.engine) as session:
            session.delete(model)
            session.commit()
            session.flush()
            return model

    def update(self, model: SQLModel):
        """
        更新数据
        :param model:
        :return:
        """
        with Session(self.engine) as session:
            session.merge(model)
            session.commit()
            session.flush()
            return model

    def query_all(self, statement):
        """
        查询全部
        :param statement:
        :return:
        """
        with Session(self.engine) as session:
            return session.exec(statement).all()

    def query_one(self, statement):
        """
        查询单个
        :param statement:
        :return:
        """
        with Session(self.engine) as session:
            return session.exec(statement).first()


if __name__ == "__main__":
    # 手写sql示例
    sql = " select * from table ;"
    db = SQLModelUtil(DBEnum.UAT, "fms")
    result = db.query_all(text(sql))
    print(result)
