# @Time    : 2025/3/8 21:15
# @Author  : MyNextWeekend
import random
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(default="haha")
    age: int = Field(default_factory=lambda: random.choice([11, 12, 13]))
    gender: Optional[str] = Field(default=None)


if __name__ == "__main__":
    user = User()
    print(user.model_dump_json())
    print(user.model_dump_json(exclude_none=True))
