import os
from io import BytesIO
from io import StringIO


def byte_io_test():
    """字节流"""
    bytes_file = BytesIO()  # 构建字节流

    bytes_file.write(b'hello world')  # 往流中写入数据
    bytes_file.write("中文".encode("utf-8"))  # 往流中写入数据

    print(f"构建字节完成: {bytes_file.getvalue()}")  # 获取流中所有数据： b'hello world\xe4\xb8\xad\xe6\x96\x87'
    bytes_file.seek(2)  # 设置指针偏移位置
    print(f'从指针位置读取数据:{bytes_file.read()}')  # b'llo world\xe4\xb8\xad\xe6\x96\x87'
    bytes_file.seek(0)  # 设置指针偏移位置
    print(bytes_file.readline())  # 读取一行数据 b'hello world\xe4\xb8\xad\xe6\x96\x87'
    print(bytes_file.readlines())  # 读取所有数据，返回一个列表，每个元素代表一行的数据

    bytes_file.close()  # 释放缓冲区


def string_io_test():
    """字符流"""
    cache_file = StringIO()

    cache_file.write('hello world')  # 往流中写入数据
    cache_file.write('中文')  # 往流中写入数据

    print(f"构建字符串完成: {cache_file.getvalue()}")  # 获取流中所有数据：hello world中文
    cache_file.seek(2)  # 设置指针偏移位置
    print(f'从指针位置读取数据:{cache_file.read()}')  # llo world中文
    cache_file.seek(0)  # 设置指针偏移位置
    print(cache_file.readline())  # 读取一行数据  hello world中文
    print(cache_file.readlines())  # 读取所有数据，返回一个列表，每个元素代表一行的数据

    cache_file.close()  # 释放缓冲区


if __name__ == '__main__':
    print(f"当前工作目录: {os.getcwd()}")
    byte_io_test()
    string_io_test()
