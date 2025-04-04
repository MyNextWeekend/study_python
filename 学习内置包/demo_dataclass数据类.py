# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 09:34
# @Author  : MyNextWeekend
from dataclasses import dataclass, field


@dataclass
class Product:
    # 名称
    name: str = field(compare=True)
    # 类别
    category: str = field(compare=True)
    # 重量
    shipping_weight: float = field(compare=False)
    # 单价
    unit_price: int = field(compare=False)
    # 税率
    tax_percent: float = field(compare=False)

    def __post_init__(self):
        """检查传入的值是否符合要求"""
        if self.shipping_weight < 0:
            raise ValueError("重量不能小于0")
        if self.unit_price < 0:
            raise ValueError("单价不能小于0")
        if not 0 < self.tax_percent < 1:
            raise ValueError("税率需要在0-1之间")

    @property
    def tax(self) -> float:
        return self.tax_percent * self.unit_price * self.shipping_weight


if __name__ == '__main__':
    banana = Product(
        name='香蕉',
        category="水果",
        shipping_weight=10.83,
        unit_price=100,
        tax_percent=0.5,
    )
    print(f"{banana.tax=}")
