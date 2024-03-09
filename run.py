import psutil

import psutil

# 获取CPU使用百分比
cpu_percent = psutil.cpu_percent()
print(f"CPU使用率11：{cpu_percent}%")

# 获取CPU逻辑核心数
cpu_count = psutil.cpu_count()
print(f"CPU逻辑核心数11：{cpu_count}")

# 获取CPU物理核心数
cpu_count_logical = psutil.cpu_count(logical=False)
print(f"CPU物理核心数：{cpu_count_logical}")

# 获取RAM总容量
ram_total = psutil.virtual_memory().total
print(f"RAM总容量：{ram_total/(1024*1024):.2f} MB")

# 获取RAM使用容量
ram_used = psutil.virtual_memory().used
print(f"RAM使用容量：{ram_used/(1024*1024):.2f} MB")

# 获取RAM可用容量
ram_available = psutil.virtual_memory().available
print(f"RAM可用容量：{ram_available/(1024*1024):.2f} MB")

# 获取RAM使用百分比
ram_percent = psutil.virtual_memory().percent
print(f"RAM使用率：{ram_percent}%")
