from pathlib import Path
from typing import List


def demo():
    # 一行代码读取文件内容
    text = Path("./path_lib_test.py").read_text()
    print(f"文件的内容是：{text}")

    path = Path("./path_lib_test.py").absolute()
    print(f"绝对路径是：{path}")
    print(f"父目录是：{path.parent}")
    print(f"拼接一个文件：{path.joinpath('test.py')}")

    # 如果文件不存在，就创建一个
    Path("./path_lib_test1.py").touch()
    # 文件路径不存在即新建，如果存在也不报错
    Path("./hello").joinpath("world").mkdir(parents=True, exist_ok=True)


def get_file_by_pattern(input_path: Path, pattern: str = "*") -> List[Path]:
    """
    获取符合指定模式的文件列表。
    :param input_path:输入路径，可以是文件或目录。
    :param pattern:匹配的文件模式，默认为 "*"。
    :return:符合模式的文件路径列表。
    """
    if not input_path.exists():
        raise FileNotFoundError(f"输入的路径不存在: {input_path}")

    # 如果是文件，直接判断是否匹配模式
    if input_path.is_file():
        return [input_path] if input_path.match(pattern) else []

    # 如果是目录，递归查找符合模式的文件
    return [item for item in input_path.rglob(pattern) if item.is_file()]
