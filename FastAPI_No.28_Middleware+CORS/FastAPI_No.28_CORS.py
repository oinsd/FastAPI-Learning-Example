# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from starlette.requests import Request
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://127.0.0.1:8888"
    
# ]

# app.add_middleware(         # 添加中间件
#     CORSMiddleware,         # CORS中间件类
#     allow_origins=origins,  # allow_origins=['*'], # 允许起源所有
#     allow_credentials=True, # 允许凭据
#     allow_methods=["*"],    # 允许方法
#     allow_headers=["*"],    # 允许头部
# )

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

