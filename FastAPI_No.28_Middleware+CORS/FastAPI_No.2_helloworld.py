# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
    
]

app.add_middleware(         # 添加中间件
    CORSMiddleware,         # CORS中间件类
    allow_origins=origins,  # 允许起源
    allow_credentials=True, # 允许凭据
    allow_methods=["*"],    # 允许方法
    allow_headers=["*"],    # 允许头部
)

@app.get("/")
async def main():
    return {"message": "Hello FastAPI, from get..."}
    
@app.post("/")
async def main1(q: str = None):
    return {"message": "Hello FastAPI, from post..."}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)

