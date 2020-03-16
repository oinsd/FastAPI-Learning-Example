# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI, HTTPException # , status
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

# 用户数据（模拟）
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True, # 关闭此用户
    },
}

app = FastAPI()

# 哈希密码（模拟）
def fake_hash_password(password: str):
    return "fakehashed" + password
# oauth2_scheme是令牌对象，token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token") # Bearer 持票人（承载、数据载体）

# 用户信息模型
class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None
# 用户输入模型
class UserInDB(User):
    hashed_password: str    #哈希密码
    username: str # 此行多余，为了vscode不报错而已。
# 获取用户
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

# 解码令牌（模拟）
def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

# 获取当前用户
# 如果用户不存在或处于非活动状态，则这两个依赖项都将仅返回HTTP错误。
async def get_current_user(token: str = Depends(oauth2_scheme)):
    print('oauth2_scheme', oauth2_scheme)
    print('token', token)
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials", # 无效的身份验证凭据
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# 获取当前活跃用户，get（read_users_me）专属
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token") # name = johndoe,alice     password = secret,secret2
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 使用username来自表单字段的从（假）数据库获取用户数据。
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # 先将这些数据放到Pydantic UserInDB模型中
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # 如果正确返回
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

