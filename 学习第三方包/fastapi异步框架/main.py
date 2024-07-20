from typing import Any, Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ItemRes(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.post("/items/", response_model=ItemRes)
async def create_item(item: ItemRes) -> Any:
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
