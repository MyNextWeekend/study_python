# @Time    : 2021/4/16 21:58
# @Author  : MyNextWeekend
import logging
from logging.handlers import TimedRotatingFileHandler

from utils.path_utils import get_path
from utils.wrapper import singleton


@singleton
class SingletonLog:
    def __init__(self):
        # 如果已经初始化了就不再执行，避免重复添加handle
        self.Flag = False
        self.fmt_str = (
            "%(asctime)s【%(levelname)s】-%(filename)s[%(lineno)d]: %(message)s"
        )
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 添加handle
        self.logger.addHandler(self.console_handle())
        self.logger.addHandler(self.file_handle())

    def file_handle(self):
        """日志文件的handle"""

        filename = get_path("logs/log.log")
        file_handle = TimedRotatingFileHandler(
            filename, when="midnight", backupCount=5, encoding="utf-8"
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
