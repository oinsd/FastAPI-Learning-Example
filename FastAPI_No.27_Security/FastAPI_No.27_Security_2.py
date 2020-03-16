# -*- coding: UTF-8 -*-
from typing import Optional

from fastapi import Depends, FastAPI, Header
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
# oauth2_scheme是令牌对象，token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print('token', token)
    print('token type', type(token))
    user = fake_decode_token(token)
    return user


@app.get("/users/me")#    Authorization: Bearer joxxxxxxx
async def read_users_me(current_user: User = Depends(get_current_user)): # Authorization: str = Header(...),
    return current_user

# 在同一文件中混合了安全性，数据模型，功能，路径操作。
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


