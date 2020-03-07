# -*- coding: UTF-8 -*-
from typing import Set,List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = set()  # 集合 创建一个空集合必须用 set() 而不是 { }
    image: Image = None # 使用子模型作为类型
    images: List[Image] = None # 带有子模型列表的属性


# 到处都有编辑器支持
@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

