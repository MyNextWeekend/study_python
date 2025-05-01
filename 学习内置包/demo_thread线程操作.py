"""
threading.local
"""

import threading
import uuid

from utils.log_utils import LogUtil

logger = LogUtil().get_logger()

# 创建一个 threading.local 对象
local = threading.local()


def do_something():
    logger.info(f"do_something get value: {local.value}")
    logger.info("func do_something end")


def process_data():
    # 为当前线程设置 thread_local 的属性
    local.value = str(uuid.uuid4())
    logger.info(f"process_data get value: {local.value}")
    do_something()
    logger.info("func process_data end")
    # 如果是在线程池中需要手动清理，避免污染
    del local.value


if __name__ == "__main__":
    # 创建并启动多个线程
    threads = []
    for _ in range(3):
        t = threading.Thread(target=process_data)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
