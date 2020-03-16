# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI
import time

app = FastAPI()
#简单介绍

async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    limit += 66
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)): 
    # 什么可以作为一个依赖？要‘可调用的’比如说类、函数、包等
    commons['skip'] += 10
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

