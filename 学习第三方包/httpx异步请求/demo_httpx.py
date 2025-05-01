import asyncio

from httpx import AsyncClient


async def get_something():
    """无需手动关闭客户端"""
    async with AsyncClient() as client:
        result = await client.get("http://httpx.org")
        print(result.text)


async def post_something():
    """手动关闭客户端"""
    client = AsyncClient()
    result = await client.post("http://httpx.org")
    print(result.text)
    await client.aclose()


if __name__ == "__main__":
    asyncio.run(post_something())
