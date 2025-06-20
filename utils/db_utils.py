from contextlib import contextmanager
from enum import Enum
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Type, Union

import pymysql
from pymysql.cursors import Cursor, DictCursor

from utils.log_utils import LogUtil

logger = LogUtil().get_logger()


class DBConf(NamedTuple):
    host: str
    port: int
    user: str
    passwd: str


class DBEnvEnum(Enum):
    """
    数据库配置
    """

    SIT = DBConf(host="127.0.0.1", port=3306, user="root", passwd="123456")
    UAT = DBConf(host="127.0.0.1", port=3306, user="root", passwd="123456")


class DBUtil:
    """
    数据库工具类，提供 事务 和 非事务 操作
    """

    def __init__(
        self, env: DBEnvEnum, database: str, cursor: Type[Cursor] = DictCursor
    ):
        logger.info(f"init db:{env.name} database:{database}")
        self._conn: pymysql.Connection = pymysql.connect(
            **env.value._asdict(),
            db=database,
            cursorclass=cursor,
        )
        # 默认不开启事务
        self._in_transaction = False

    @contextmanager
    def transaction(self):
        self._in_transaction = True
        try:
            logger.info("will begin transaction")
            self._conn.begin()
            yield self
            logger.info("commit changes in transaction")
            self._conn.commit()
        except Exception as e:
            logger.error(f"will rollback in transaction: {e}")
            self._conn.rollback()
            raise e
        finally:
            self._in_transaction = False

    def execute(
        self, sql: str, param: Optional[Union[Tuple, List, Dict]] = None
    ) -> int:
        logger.info(f"execute sql:{sql} ,params:{param}")
        with self._conn.cursor() as cursor:
            result = cursor.execute(sql, param)
            if not self._in_transaction:
                self._conn.commit()
                logger.info("commit changes successfully")
            return result

    def execute_many(self, sql: str, params: List[Union[Tuple, List, Dict]]) -> int:
        logger.info(f"executemany sql:{sql} ,params:{params}")
        with self._conn.cursor() as cursor:
            result = cursor.executemany(sql, params)
            if not self._in_transaction:
                self._conn.commit()
                logger.info("commit changes successfully")
            return result

    def fetch_one(
        self, sql: str, params: Optional[Union[Tuple, List, Dict]] = None
    ) -> Optional[Dict[str, Any]]:
        logger.info(f"execute sql:{sql} ,params:{params}")
        with self._conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchone()

    def fetch_all(
        self, sql: str, params: Optional[Union[Tuple, List, Dict]] = None
    ) -> List[Dict[str, Any]] | tuple[tuple[Any, ...], ...]:
        logger.info(f"execute sql:{sql} ,params:{params}")
        with self._conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    def fetch_many(
        self, sql: str, size: int, params: Optional[Union[Tuple, List, Dict]] = None
    ) -> List[Dict[str, Any]] | tuple[tuple[Any, ...], ...]:
        logger.info(f"execute sql:{sql} ,params:{params}")
        with self._conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchmany(size)


if __name__ == "__main__":
    db = DBUtil(DBEnvEnum.SIT, "first")

    # 非事务性操作
    db.execute("""CREATE TABLE if not EXISTS  accounts (
        id BIGINT AUTO_INCREMENT PRIMARY KEY, -- 主键，自动增长
        username VARCHAR(255) NOT NULL UNIQUE, -- 用户名，唯一且非空
        password_hash VARCHAR(255) NOT NULL, -- 密码的哈希值
        salt VARCHAR(64), -- 密码加盐值（如果需要）
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 记录创建时间
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- 记录更新时间
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)

    # 事务操作，有任何异常即回滚
    with db.transaction() as obj:
        obj.execute(
            "insert into accounts (username, password_hash)values ('1001','123456');"
        )
        obj.execute(
            "insert into accounts (username, password_hash)values ('1002','654321');"
        )

    res = db.fetch_all("select * from accounts")
    logger.info(f"查询结果数量是:{len(res)},查询结果是:{res}")
