import importlib
import inspect
import os


def import_and_parse_py_files(directory: str, package: str = None):
    """
    递归导入指定目录下的所有 .py 文件，使用 inspect 解析模块信息。

    :param directory: 目标文件夹路径。
    :param package: 如果需要相对导入，指定顶层包的名称。
    :return: 一个字典，键为模块名，值为模块的解析信息（类、函数、变量）。
    """
    imported_modules = {}

    # 遍历目录和子目录
    for root, _, files in os.walk(directory):
        for file in files:
            # 跳过非 .py 文件
            if not file.endswith(".py"):
                continue

            # 构造模块名
            relative_path = os.path.relpath(root, directory)
            module_name = file[:-3]  # 去掉 .py 扩展名
            if relative_path != ".":
                module_name = f"{relative_path.replace(os.sep, '.')}.{module_name}"
            if package:
                full_module_name = f"{package}.{module_name}"
            else:
                full_module_name = module_name

            try:
                # 使用 importlib 导入模块
                print(f"{directory}.{full_module_name}")
                module = importlib.import_module(f"{directory}." + full_module_name)
                imported_modules[full_module_name] = parse_module(module)
            except Exception as e:
                print(f"无法导入模块 {full_module_name}: {e}")

    return imported_modules


def parse_module(module):
    """
    使用 inspect 解析模块中的类、函数、变量。

    :param module: 导入的模块对象。
    :return: 包含模块中类、函数、变量的字典。
    """
    module_info = {"classes": [], "functions": [], "variables": []}

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__ == module.__name__:
            module_info["classes"].append(name)
        elif inspect.isfunction(obj) and obj.__module__ == module.__name__:
            module_info["functions"].append(name)
        elif (
            not inspect.ismodule(obj)
            and not inspect.isfunction(obj)
            and not inspect.isclass(obj)
        ):
            module_info["variables"].append(name)

    return module_info


# 示例用法
if __name__ == "__main__":
    target_directory = "学习第三方包"  # 替换为你的目标目录
    top_level_package = None  # 如果是包，填入顶层包名，例如 "my_project"

    parsed_modules = import_and_parse_py_files(
        target_directory, package=top_level_package
    )

    # 打印解析结果
    for module_name, module_info in parsed_modules.items():
        print(f"模块: {module_name}")
        print("  类:", module_info["classes"])
        print("  函数:", module_info["functions"])
        print("  变量:", module_info["variables"])
