import asyncio
import uuid
from contextvars import ContextVar

# 声明一个上下文变量，指定默认值为 0
trace_id: ContextVar[str] = ContextVar("trace_id", default="-")


async def set_trace_id():
    trace_id.set(f"{uuid.uuid4()}")


async def func_001():
    print(f"func 001 trace_id: {trace_id.get()}")


async def func_002():
    print(f"func 002 trace_id: {trace_id.get()}")


async def func_003():
    print(f"func 003 trace_id: {trace_id.get()}")


async def func_a():
    await set_trace_id()
    await func_001()
    await func_002()
    await func_003()


async def main():
    await asyncio.gather(func_a(), func_a())  # 两个协程同时运行


if __name__ == "__main__":
    asyncio.run(main())
