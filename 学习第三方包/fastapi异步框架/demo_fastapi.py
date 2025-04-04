from typing import Any, Union

from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

from utils.log_utils import SingletonLog

log = SingletonLog().get_logger()
app = FastAPI()


class ItemRes(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(file: UploadFile) -> Any:
    log.info(f"收到文件的名称是：{file.filename}")
    log.info(f"收到文件的大小是：{file.size}")
    contents = await file.read()
    return contents


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
