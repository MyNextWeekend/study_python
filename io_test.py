from datetime import datetime
import os

print(os.getcwd())
print(datetime.now())

a = """zhegeshiyige"""
print(a)
# 类似文件的缓冲区
from io import BytesIO
bytes_file = BytesIO()
bytes_file.write(b'hello world')
bytes_file.seek(0)
print(bytes_file.read()) # b'hello world'
bytes_file.close()


from io import StringIO
cache_file = StringIO()
print(cache_file.write('hello world')) # 11
print(cache_file.seek(0)) # 0
print(cache_file.read()) # hello world
print(cache_file.close())  # 释放缓冲区