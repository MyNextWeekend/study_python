import asyncio
import time

"""
优点：原生支持，不需要下载第三方包
缺点：代码中如果用到第三方包需要第三方包也实现异步，否则效果还是同步
"""


async def do_something(number: int) -> int:
    print(f"do_something func start {number} at {time.strftime('%X')}")
    if number % 2 == 0:
        raise ValueError("odd number")
    await asyncio.sleep(number)
    print(f"do_something func end {number} at {time.strftime('%X')}")
    return number


async def demo_task_group():
    print(f"demo_task_group func start at {time.strftime('%X')}")

    # 有一个方法抛异常，其他没有执行完的协程都停止了
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(do_something(5))
        t2 = tg.create_task(do_something(2))

        print(f"started at {time.strftime('%X')}")

    print(f"t1:{t1.result()},t2:{t2.result()}")
    print(f"demo_task_group func finished at {time.strftime('%X')}")


async def demo_time_out():
    print(f"demo_time_out func start at {time.strftime('%X')}")

    try:
        async with asyncio.Timeout(5):
            await do_something(7)
    except TimeoutError:  # 引发异常的时候，方法可能没有执行完成
        print("time out error")
    await asyncio.sleep(5)
    print(f"demo_time_out func finished at {time.strftime('%X')}")


async def demo_gather():
    print(f"demo_gather func start at {time.strftime('%X')}")
    await asyncio.gather(do_something(3), do_something(5))  # 两个协程同时运行
    print(f"demo_gather func finished at {time.strftime('%X')}")


if __name__ == "__main__":
    # asyncio.run(demo_gather())
    # asyncio.run(demo_task_group())
    asyncio.run(demo_time_out())
