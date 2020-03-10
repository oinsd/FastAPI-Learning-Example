# -*- coding: UTF-8 -*-
from fastapi import FastAPI
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import JSONResponse

# 安装自定义异常处理程序
# 自定义异常UnicornException
class UnicornException(Exception):  # Exception 常规错误的基类
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=404, # 418 I'm a teapot
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)