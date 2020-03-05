# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from enum import Enum

class Name(str, Enum):
    Allan = '张三'
    Jon   = '李四'
    Bob   = '王五'

app = FastAPI()


@app.get("/{who}")
async def get_day(who: Name):
    if who == Name.Allan:
        return {"who": who, "message": "张三是德国人"}
    if who.value == '李四':
        return {"who": who, "message": "李四是英国人"}
    return {"who": who, "message": "王五是法国人"}


@app.get("/")
async def main():
    return {"message": "Hello，FastAPI"}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)