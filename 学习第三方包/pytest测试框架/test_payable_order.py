# -*- coding: utf-8 -*-
# @Time    : 2024/11/23 23:14
# @Author  : hejinhu
import logging

import pytest

logger = logging.getLogger(__name__)


def get_params():
    logger.info("此处执行了方法:--------------------------")
    import random
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return [("张三", a), ("李四", b)]


def test_payable_order(login):
    logger.info("test_payable_order")
    assert True


@pytest.mark.parametrize("name,password", get_params())
def test_parm(name, password):
    import time
    time.sleep(2)
    logger.info(f"test_parm1 {name}::{password}")
    logger.info(f"test_parm2 {name}::{password}")
    logger.info(f"test_parm3 {name}::{password}")
    assert True
