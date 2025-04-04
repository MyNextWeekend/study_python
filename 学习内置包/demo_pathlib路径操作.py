import pathlib

# 一行代码读取文件内容
text = pathlib.Path("./path_lib_test.py").read_text()
print(f"文件的内容是：{text}")

path = pathlib.Path("./path_lib_test.py").absolute()
print(f"绝对路径是：{path}")
print(f"父目录是：{path.parent}")
print(f"拼接一个文件：{path.joinpath('test.py')}")

# 如果文件不存在，就创建一个
# pathlib.Path("./path_lib_test1.py").touch()
# 文件路径不存在即新建，如果存在也不报错
# pathlib.Path("./hello").joinpath("world").mkdir(parents=True, exist_ok=True)
