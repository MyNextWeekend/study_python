from sqlacodegen.generators import SQLModelGenerator
from sqlalchemy import MetaData, create_engine

"""
sqlacodegen 自动生成数据库到python的表结构映射
"""
# 方案一：手动执行命令生成py文件
comm = "sqlacodegen --generator sqlmodels mysql+pymysql://root:123456@localhost:3306/fms > fms.py"


# 方案二：通过代码调用
def get_table_info():
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/fms")
    metadata = MetaData()
    generator = SQLModelGenerator(metadata, engine, {})
    metadata.reflect(engine, None, False, None)
    return generator.generate()


def write_file(info: str, file: str):
    with open(file, "w") as f:
        f.write(info)


if __name__ == "__main__":
    table_info = get_table_info()
    print(table_info)
    # write_file(table_info, "sqlmodels_test.py")
