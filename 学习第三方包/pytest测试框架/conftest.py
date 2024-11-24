# -*- coding: utf-8 -*-
# @Time    : 2024/11/23 23:14
# @Author  : hejinhu
import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.fixture
def login():
    logger.info("登录")


def pytest_runtest_logreport(report):
    logger.info(f"获取到的日志是：{report.caplog}")
    logger.info(f"运行类型是：{report.when}")
    logger.info(f"运行用例花费的时间：{report.duration:.4f}秒")
