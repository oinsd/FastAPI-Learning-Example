# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import jwt
from fastapi import Depends, FastAPI, HTTPException # , status
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext # passlib 处理哈希加密的包
from pydantic import BaseModel

# to get a string like this run: openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"# 密钥
ALGORITHM = "HS256"     # 算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30    # 访问令牌过期分钟

# 用户数据（模拟）
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}



class Token(BaseModel):     # 令牌空壳
    access_token: str
    token_type: str
class TokenData(BaseModel): # 令牌数据
    username: str = None
class User(BaseModel):      # 用户基础模型
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None
class UserInDB(User):       # 用户输入数据模型
    hashed_password: str
    username: str           # 此行多余，为了vscode不报错而已。
# Context是上下文  CryptContext是密码上下文   schemes是计划     deprecated是不赞成（强烈反对）
# bcrypt是加密算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme是令牌对象，token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
app = FastAPI()



# verify_password验证密码   plain_password普通密码      hashed_password哈希密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
# 获取密码哈希
def get_password_hash(password):
    return pwd_context.hash(password)
# 获取用户
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
# 验证用户
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print('验证用户user :', user)
    print('验证用户type :', type(user))
    return user  # <class '__main__.UserInDB'>




# 创建访问令牌
def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta # expire 令牌到期时间 
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



# 获取当前用户
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    print('获取当前用户user :', user)
    print('获取当前用户type :', type(user))
    return user
# 获取当前激活用户
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user




# name = johndoe    password = secret
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 1、验证用户
    user = authenticate_user(fake_users_db, form_data.username, form_data.password) # 验证用户
    # 2、access_token_expires访问令牌过期
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # timedelta表示两个datetime对象之间的差异。（来自datetime包）
    # 3、create_access_token创建访问令牌
    access_token = create_access_token(data={"sub": user.username}, 
                                expires_delta=access_token_expires)
    # 返回
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]






if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

