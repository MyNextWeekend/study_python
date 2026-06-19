import ast
import pathlib
from dataclasses import dataclass
from typing import Optional


@dataclass
class Arg:
    name: str
    type: Optional[str]


@dataclass
class FuncInfo:
    func_name: str
    args: list[Arg]


@dataclass
class AstInfo:
    is_class: bool
    class_name: Optional[str]
    functions: list[FuncInfo]


def _get_parameters_with_types(func: ast.FunctionDef) -> list[Arg]:
    """
    获取方法的形参及其类型注解。
    :param func:
    :return:
    """
    parameters = []
    for parameter in func.args.args:
        arg_name = parameter.arg
        # if arg_name == "self":  # 过滤 方法的 self 参数
        #     continue
        arg = Arg(name=arg_name, type=None)
        if parameter.annotation:
            type_annotation = ast.unparse(parameter.annotation)
            arg.type = type_annotation
        parameters.append(arg)
    return parameters


def extract_function_parameters_with_types(file_path: pathlib.Path):
    """
    解析给定的 Python 源代码，提取函数形参及其类型注解。
    :param file_path: 文件路径
    :return:
    """
    functions = []
    class_functions = []

    with open(file_path) as f:
        node = ast.parse(f.read())

    for stmt in node.body:
        if isinstance(stmt, ast.FunctionDef):  # 普通方法
            function_name = stmt.name
            args = _get_parameters_with_types(stmt)
            functions.append(FuncInfo(func_name=function_name, args=args))
        if isinstance(stmt, ast.ClassDef):  # 类
            class_name = stmt.name
            ast_info = AstInfo(is_class=True, class_name=class_name, functions=[])
            for class_stmt in stmt.body:
                if isinstance(class_stmt, ast.FunctionDef):
                    name = class_stmt.name
                    # if name == "__init__":  # 去掉初始化方法
                    #     continue
                    ast_info.functions.append(
                        FuncInfo(
                            func_name=name,
                            args=_get_parameters_with_types(class_stmt),
                        )
                    )
            class_functions.append(ast_info)

    return AstInfo(
        is_class=False, class_name=None, functions=functions
    ), class_functions


if __name__ == "__main__":
    path = pathlib.Path(__file__)
    file1 = path.parent / "demo_datetime时间模块.py"
    file2 = path.parent / "demo_protocol鸭子类型.py"
    print(extract_function_parameters_with_types(file1))
    # (['get_before_date(days: int, today: datetime.date)', 'get_before_datetime(days: int, today_time: datetime.datetime)', 'get_before_time(today_time: datetime.datetime, day: int, hour: int, minute: int, second: int)'], [])
    print(extract_function_parameters_with_types(file2))
    # (['do_something(animal: Animal)'], ['Animal.eat(self)', 'Animal.drink(self)', 'Dog.eat(self)', 'Dog.drink(self)', 'Cat.eat(self)'])
