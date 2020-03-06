# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    print(item.dict())
    return item,'人生没有无意义的经历。'

@app.put("/items/{item_id}")
async def create_item2(item_id: int, item: Item, q: str = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    print(result)
    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

