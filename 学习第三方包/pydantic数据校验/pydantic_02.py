from pydantic import BaseModel, PositiveFloat, PositiveInt, Field


class Product(BaseModel):
    # 名称
    name: str
    # 类别
    category: str
    # 重量
    shipping_weight: PositiveFloat
    # 单价
    unit_price: PositiveInt
    # 税率
    tax_percent: float = Field(ge=0, le=1)

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
    print(f"{banana.model_dump()}")
