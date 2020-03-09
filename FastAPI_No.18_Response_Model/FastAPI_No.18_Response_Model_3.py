# -*- coding: UTF-8 -*-
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.88, "tags": []},
}

# response_model_exclude_unset=True 些默认值将不包括在响应中，仅包含实际设置的值。
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
    
# response_model_exclude={"tax"} 是排除tax
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"price"})
async def read_item_public_data(item_id: str):
    return items[item_id]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)