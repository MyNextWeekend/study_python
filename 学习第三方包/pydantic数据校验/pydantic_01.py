from datetime import datetime
from typing import Generic, Self, TypeVar

from pydantic import (
    BaseModel,
    PositiveInt,
    field_serializer,
    field_validator,
    model_validator,
)


class User(BaseModel):
    id: int
    name: str = "John Doe"
    nickname: str
    age: int
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

    @field_serializer("signup_ts")
    def serialize_ts(self, dt: datetime, _info):
        """序列化的时候调用"""
        return datetime.strftime(dt, "%Y-%m-%d %H:%M:%S")

    @field_validator("age")
    def good(cls, value):
        """自定义检查字段"""
        if value < 18:
            raise ValueError("年龄必须大于18岁")
        return value

    @model_validator(mode="after")
    def verify_square(self) -> Self:
        """用于比较多个字段"""
        if self.name == self.nickname:
            raise ValueError("姓名和别名不能一样")
        return self


T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    code: int
    msg: str
    data: T


external_data = {
    "code": 200,
    "msg": "ok",
    "data": {
        "id": 123,
        "age": 22,
        "nickname": "John",
        "signup_ts": "2019-06-01 12:22",
        "tastes": {
            "wine": 9,
            "cheese": 7,
            "cabbage": "1",
        },
        "other": "haha",  # 多余的字段不影响转换
    },
}

# 从字典 创建对象
user = Response[User].model_validate(external_data)
print(f"{user.data.id=}")
print(f"{user.data.name=}")

# 返回一个字典
user_dic = user.model_dump()
print(f"{user_dic=}")

# 对象 序列化成 字符串
user_json = user.model_dump_json()
print(f"{user_json=}")
