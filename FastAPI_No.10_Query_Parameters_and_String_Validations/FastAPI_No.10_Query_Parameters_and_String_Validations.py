# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()
#########################################################
# 限制长度
@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3, max_length=50)):    
    #填None就是默认值   填 ...则是必填项 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#########################################################
#正则表达式
@app.get("/items2/")
async def read_items2(
                        q: str = Query(None, min_length=3, max_length=50, regex="^nice")
                     ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#########################################################
#列表
@app.get("/items3/")
async def read_items3(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items
#########################################################
#别名参数
@app.get("/items4/")
async def read_items4(q: str = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#########################################################
#弃用参数
@app.get("/items5/")
async def read_items5(
    q: str = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#########################################################



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

