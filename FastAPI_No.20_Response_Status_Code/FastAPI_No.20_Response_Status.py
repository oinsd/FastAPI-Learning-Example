# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from starlette import status

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

@app.get("/items2/", status_code=201)
async def create_item2(name: str):
    return {"name": name}

@app.post("/items3/", status_code=status.HTTP_404_NOT_FOUND)
async def create_item3(name: str):
    print('HTTP_404:', status.HTTP_404_NOT_FOUND)
    return {"name": name}

@app.get("/i/", status_code=status.HTTP_404_NOT_FOUND)
async def i(name: str):
    print('HTTP_404:', status.HTTP_404_NOT_FOUND)
    return {"name": name}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)