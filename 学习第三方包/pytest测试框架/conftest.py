# @Time    : 2024/11/23 23:14
# @Author  : hejinhu
import logging

import pytest
from pytest import CallInfo, Item, TestReport

logger = logging.getLogger(__name__)


@pytest.fixture
def login():
    logger.info("登录")


def pytest_collection_modifyitems(session, config, items):
    """
    收集所有测试用例并存储到全局变量中。
    """
    collected_tests = []  # 清空之前的收集记录

    for index, item in enumerate(items):
        # 记录测试用例信息
        collected_tests.append(
            {
                "index": index,
                "name": item.name,
                "nodeid": item.nodeid,
                "function": item.function,
            }
        )

    # 打印所有收集的测试用例
    print("\nCollected Test Methods:")
    for test in collected_tests:
        print(f"{test['index']}: {test['nodeid']}")

    # 获取用户的选择修改测试用例
    selected_indices = config.getoption("--select-tests")
    if selected_indices is None:
        items[:] = []


def pytest_addoption(parser):
    """
    添加自定义命令行选项。
    """
    parser.addoption(
        "--select-tests",
        action="store",
        default=None,
        help="Comma-separated list of test indices to run",
    )


# def pytest_runtest_logreport(report: TestReport) -> None:
#     logger.info(f"获取到的日志是：{report.caplog}")
#     logger.info(f"运行类型是：{report.when}")
#     logger.info(f"运行用例花费的时间：{report.duration:.4f}秒")


def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> TestReport | None:
    logger.info(f"{item=}")
