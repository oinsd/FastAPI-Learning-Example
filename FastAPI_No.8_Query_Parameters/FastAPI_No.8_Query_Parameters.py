# -*- coding: UTF-8 -*-
from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/i/")
async def i(A: str = 'HI..', B: str = 'Hello..', C: str = 'He..'):
    return {'cc': A+B+C},{'dd': B+C}
    
@app.get("/ii/")
async def ii(A: int = 0, B: int = 10, C: int = 20):
    return {'cc': A+B+C},{'dd': B+C}

@app.get("/iii/")
async def iii(A: int = 0, B: int = 10, C: int = 20):
    return 'A+B+C',A+B+C
   
# bool与类型转换
@app.get("/xxx/{item_id}")
async def xxx(item_id: str, QQ: str = None, SS: bool = False):
    item = {"item_id": item_id}
    if QQ:
        item.update({"QQ": QQ})
    if not SS:  # 如果SS是假
        item.update(
            {"item_id": "This is SSSSSSS"}
        )
    return item

#多路径 和 查询参数 和 必填字段
@app.get("/user/{user_id}/item/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

