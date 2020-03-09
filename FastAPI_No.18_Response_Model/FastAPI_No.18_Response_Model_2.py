# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


@app.post("/user/", response_model=UserOut)
async def create_user(*, user: UserIn):
    return user


# pip install pydantic[email]
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)