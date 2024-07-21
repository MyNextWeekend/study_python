from typing import Any, Union, Optional

from fastapi import FastAPI
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


@app.post("/items/", response_model=ItemRes)
async def create_item(item: ItemRes) -> Any:
    log.info(item)
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
