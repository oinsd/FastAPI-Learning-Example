# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException # , status
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext # passlib 处理哈希加密的包
from pydantic import BaseModel



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# verify_password验证密码   plain_password普通密码      hashed_password哈希密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
# 获取密码哈希
def get_password_hash(password):
    return pwd_context.hash(password)


if __name__ == "__main__":
    ############################本章节哈希验证用法############################
    xxx = get_password_hash('cccccc')
    yyy = get_password_hash('cccccc')
    print(xxx)
    print(yyy)
    print('verify_password',verify_password('cccccc',xxx))
    print('verify_password',verify_password('cccccc',yyy))
    print('verify_password',verify_password('secret','$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW'))



    ############################本章节时间差（timedelta）用法###########################
    from datetime import datetime
    from datetime import timedelta
    aDay = timedelta(minutes=30) # timedelta表示两个datetime对象之间的差异。（来自datetime包）
    now = datetime.now() + aDay
    print(aDay)
    print(datetime.now())
    print(now ,type(now))
    
    