import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


async def run_fastapi():
    import uvicorn

    # 在这里启动FastAPI服务器
    config = uvicorn.Config(app, host="127.0.0.1", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


async def background_task():
    while True:
        print("主线任务正在运行...")
        await asyncio.sleep(3)  # 每3秒执行一次


async def main():
    # 启动FastAPI服务器
    _ = asyncio.create_task(run_fastapi())

    # 启动主线任务
    await background_task()


if __name__ == "__main__":
    asyncio.run(main())
