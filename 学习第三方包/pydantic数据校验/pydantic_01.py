import json
from datetime import datetime
from typing import Self

from pydantic import BaseModel, PositiveInt, field_validator, model_validator, field_serializer


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    nickname: str
    age: int
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

    @field_serializer('signup_ts')
    def serialize_ts(self, dt: datetime, _info):
        """序列化的时候调用"""
        return datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')

    @field_validator('age')
    @classmethod
    def good(cls, value):
        """自定义检查字段"""
        if value < 18:
            raise ValueError("年龄必须大于18岁")
        return value

    @model_validator(mode='after')
    def verify_square(self) -> Self:
        """用于比较多个字段"""
        if self.name == self.nickname:
            raise ValueError('姓名和别名不能一样')
        return self


external_data = {
    'id': 123,
    "age": 22,
    "nickname": "John",
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        'cheese': 7,
        'cabbage': '1',
    },
}

# 从字典解包创建对象
user = User(**external_data)
print(f"{user.id=}")

# 返回一个字典
user_dic = user.model_dump()
print(f"{user_dic=}")

# 对象 序列化成 字符串
user_json = user.model_dump_json()
print(f"{user_json=}")

# 从json字符串 反序列化 成对象
user = User.parse_raw(user_json)
print(f"{user.id=}")
