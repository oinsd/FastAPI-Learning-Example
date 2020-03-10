# -*- coding: UTF-8 -*-
from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
# FastAPI、starlette都有自己的HTTPException，
# 区别是，FastAPI的HTTPException允许您添加要包含在响应头。OAuth 2.0和某些安全实用程序在内部需要/使用此功能。
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {exc}")
    return await http_exception_handler(request, exc) # 重用Starlette的异常处理程序


@app.exception_handler(RequestValidationError) 
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc) # 重用FastAPI的异常处理程序


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.") # 418 I'm a teapot
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)