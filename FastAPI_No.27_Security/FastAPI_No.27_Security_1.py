# -*- coding: UTF-8 -*-
from typing import Optional

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
# 声明该URL是客户端应用于获取令牌的URL。该信息在OpenAPI中使用，然后在交互式API文档系统中使用。
# 该oauth2_scheme变量的一个实例OAuth2PasswordBearer，但它也是一个“通知”。
# oauth2_scheme是令牌对象，token: str = Depends(oauth2_scheme)后就是之前加密的令牌

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
# 尚未验证令牌的有效性


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

