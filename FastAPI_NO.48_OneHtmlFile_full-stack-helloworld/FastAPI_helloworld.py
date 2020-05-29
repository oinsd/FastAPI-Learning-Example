# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(         # 添加中间件
    CORSMiddleware,         # CORS中间件类
    allow_origins=["*"],  # 允许起源
    allow_credentials=True, # 允许凭据
    allow_methods=["*"],    # 允许方法
    allow_headers=["*"],    # 允许头部
)


@app.get("/")
async def main():
    return {"message": "Hello , this is FastAPI."}

@app.get("/{a}")
async def regist(a):
    print('前端数据是：',a)
    # print(type(a))
    return a
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

