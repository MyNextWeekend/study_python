import ast


def get_parameters_with_types(func: ast.FunctionDef):
    """
    获取方法的形参及其类型注解。
    :param func:
    :return:
    """
    parameters = []
    for parameter in func.args.args:
        arg_name = parameter.arg
        if parameter.annotation:
            type_annotation = ast.unparse(parameter.annotation)
            arg_name += f": {type_annotation}"
        parameters.append(arg_name)
    return ", ".join(parameters)


def extract_function_parameters_with_types(file_path: str):
    """
    解析给定的 Python 源代码，提取函数形参及其类型注解。
    :param file_path: 文件路径
    :return:
    """
    functions = []
    class_functions = []

    with open(file_path, "r") as f:
        node = ast.parse(f.read())

    for stmt in node.body:
        if isinstance(stmt, ast.FunctionDef):  # 普通方法
            function_name = stmt.name
            args_str = get_parameters_with_types(stmt)
            functions.append(f"{function_name}({args_str})")
        if isinstance(stmt, ast.ClassDef):  # 类
            class_name = stmt.name
            for class_stmt in stmt.body:
                if isinstance(class_stmt, ast.FunctionDef):
                    args_str = get_parameters_with_types(class_stmt)
                    class_functions.append(f"{class_name}.{class_stmt.name}({args_str})")

    return functions, class_functions


if __name__ == '__main__':
    file1 = "datetime时间模块.py"
    file2 = "protocol鸭子类型.py"
    print(extract_function_parameters_with_types(file1))
    # (['get_before_date(days: int, today: datetime.date)', 'get_before_datetime(days: int, today_time: datetime.datetime)', 'get_before_time(today_time: datetime.datetime, day: int, hour: int, minute: int, second: int)'], [])
    print(extract_function_parameters_with_types(file2))
    # (['do_something(animal: Animal)'], ['Animal.eat(self)', 'Animal.drink(self)', 'Dog.eat(self)', 'Dog.drink(self)', 'Cat.eat(self)'])
