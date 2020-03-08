# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get", ge=50, le=100),#ge 大于等于 gt是大于 le是小于等于
    q: str       = Query(None, alias="item-query"),
    size: float  = Query(1, gt=0, lt=10.5)
                    ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

