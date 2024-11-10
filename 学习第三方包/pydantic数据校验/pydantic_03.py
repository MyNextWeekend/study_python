import json
from dataclasses import dataclass, field, asdict
from enum import StrEnum
from typing import List, Union, Tuple


class SearchOperationEnum(StrEnum):
    GREATER_THAN = "gt"
    GREATER_THAN_EQUAL = "gte"
    LESS_THAN = "lt"
    LESS_THAN_EQUAL = "lte"
    EQUAL = "eq"
    NOT_EQUAL = "ne"
    IN_LIST = "in"
    NOT_IN = "not in"
    LIKE = "like"
    NOT_LIKE = "not like"
    RANGE = "range"


@dataclass
class FieldCondition:
    # 字段名称
    field_name: str
    # 搜索操作类型
    operation: SearchOperationEnum
    # 搜索值
    value: Union[str, int, float, Tuple[Union[str, int, float], Union[str, int, float]]]


@dataclass
class SearchModel:
    conditions: List[FieldCondition] = field(default_factory=list)

    def to_json(self):
        dict_model = asdict(self)

        for condition in dict_model["conditions"]:
            condition["operation"] = condition["operation"].value

        return json.dumps(dict_model["conditions"])


if __name__ == '__main__':
    # 创建一些搜索条件
    price_condition = FieldCondition(
        field_name="price",
        operation=SearchOperationEnum.RANGE,
        value=(100, 500)
    )

    date_condition = FieldCondition(
        field_name="date",
        operation=SearchOperationEnum.GREATER_THAN,
        value="2024-01-01"
    )

    name_condition = FieldCondition(
        field_name="name",
        operation=SearchOperationEnum.LIKE,
        value="Alice"
    )

    # 创建 SearchModel 并添加条件
    search_model = SearchModel(conditions=[price_condition, date_condition, name_condition])

    # 将 SearchModel 转换为 JSON
    json_output = search_model.to_json()
    print(json_output)
