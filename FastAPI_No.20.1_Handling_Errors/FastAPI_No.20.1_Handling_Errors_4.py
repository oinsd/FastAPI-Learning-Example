# -*- coding: UTF-8 -*-
from fastapi import FastAPI
# from fastapi import FastAPI, Request, status
from starlette.requests import Request
from starlette import status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.exception_handler(RequestValidationError)  # 请求验证错误
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)