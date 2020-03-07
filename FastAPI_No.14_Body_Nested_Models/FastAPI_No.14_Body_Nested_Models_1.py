# -*- coding: UTF-8 -*-
from typing import List, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str  = None
    price: float
    tax: float        = None
    tags0: list       = []
    tags1: List[str]  = []
    tags2: Set[str]   = set()


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

