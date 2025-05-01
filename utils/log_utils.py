# @Time    : 2021/4/16 21:58
# @Author  : MyNextWeekend
import logging
import uuid
from contextvars import ContextVar
from logging.handlers import TimedRotatingFileHandler

from config.config import settings
from utils.wrapper import singleton

# 声明上下文变量（不管是同步还是异步，都可以使用）
# 子线程不会继承父线程的上下文，需要手动copy_context
trace_id: ContextVar[str] = ContextVar("trace_id", default="-")


class TraceIdFilter(logging.Filter):
    def filter(self, record):
        # 将当前上下文中的 trace_id 注入到日志记录中
        record.trace_id = trace_id.get() or "-"
        if "-" == record.trace_id:
            trace_id_new = str(uuid.uuid4()).replace("-", "")
            trace_id.set(trace_id_new)
            record.trace_id = trace_id_new
        return True


@singleton
class LogUtil:
    def __init__(self):
        # 如果已经初始化了就不再执行，避免重复添加handle
        self.Flag = False
        self.fmt_str = "%(asctime)s【%(levelname)s】-%(filename)s[%(lineno)d][%(trace_id)s]: %(message)s"
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 添加handle
        self.logger.addHandler(self.console_handle())
        self.logger.addHandler(self.file_handle())
        # 添加
        self.logger.addFilter(TraceIdFilter())

    def file_handle(self):
        """日志文件的handle"""
        file_handle = TimedRotatingFileHandler(
            settings.log_file, when="midnight", backupCount=5, encoding="utf-8"
        )
        file_handle.setLevel(logging.INFO)
        fmt = logging.Formatter(self.fmt_str)
        file_handle.setFormatter(fmt)
        return file_handle

    def console_handle(self):
        """控制台日志的handle"""
        console_handle = logging.StreamHandler()
        console_handle.setLevel(logging.DEBUG)
        fmt = logging.Formatter(self.fmt_str)
        console_handle.setFormatter(fmt)
        return console_handle

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    logger = LogUtil().get_logger()
    logger.info("hello_001")
    logger.warning("hello_002")
    logger.error("hello_003")
