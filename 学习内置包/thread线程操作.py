"""
threading.local
"""

import threading

# 创建一个 threading.local 对象
thread_local_data = threading.local()


# 定义一个线程执行的函数
def process_data():
    # 为当前线程设置 thread_local_data 的属性
    thread_local_data.value = threading.current_thread().name
    print(f"Thread: {thread_local_data.value}")


# 创建并启动多个线程
threads = []
for i in range(3):
    t = threading.Thread(target=process_data)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
