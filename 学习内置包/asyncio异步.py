import asyncio

"""
优点：原生支持，不需要下载第三方包
缺点：代码中如果用到第三方包需要第三方包也实现异步，否则效果还是同步
"""


async def func_a():
    print("func_a start...")
    await asyncio.sleep(3)  # 协程让出cpu权限
    print("func_a end...")


async def main():
    await asyncio.gather(func_a(), func_a())  # 两个协程同时运行


if __name__ == '__main__':
    asyncio.run(main())
