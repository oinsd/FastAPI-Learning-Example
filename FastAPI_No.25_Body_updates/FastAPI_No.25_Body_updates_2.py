# -*- coding: UTF-8 -*-
from typing import List

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]                           # 存储项目数据
    stored_item_model = Item(**stored_item_data)                # 存储项目模型
    update_data = item.dict(exclude_unset=True)                 
    print('update_data', update_data)#################
    updated_item = stored_item_model.copy(update=update_data)
    # print('update_item', update_item)
    print('updated_item', jsonable_encoder(updated_item))#################
    items[item_id] = jsonable_encoder(updated_item)
    print('items[item_id]', items[item_id])###########
    return updated_item


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
