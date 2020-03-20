from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Boolean, Column, Integer, String

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    数据库操作初始化    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
SQLALCHEMY_DATABASE_URL = "sqlite:///db_test_1.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# 仅适用于SQLite。其他数据库不需要。 链接参数：检查同一条线？ 即需要可多线程

# 通过sessionmaker得到一个类，一个能产生session的工厂。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
             # 会话生成器   自动提交            自动刷新
Base = declarative_base() # 数据表的结构用 ORM 的语言描述出来

class M_User(Base):  #声明数据库某表的属性与结构
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # 主键
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) 
    is_active = Column(Boolean, default=True)

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

Base.metadata.create_all(bind=engine) # 到这里就会新建数据库和表（原来没有）

app = FastAPI()

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    数据库操作（依赖项）    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
def get_db():
    try:
        db = SessionLocal() # 这时，才真正产生一个'会话'，并且用完要关闭
        yield db            # 调用该函数将返回generator可迭代对象
    finally:
        db.close()
        print('数据库已关闭')
    

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    数据库操作方法    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
# 通过id查询用户信息
def get_user(db: Session, user_id: int):
    CCCCCC = db.query(M_User).filter(M_User.id == user_id).first()
    print('CCCCCC :', CCCCCC) # 过滤器
    return CCCCCC


if __name__ == "__main__":
    for i in get_db():
        c = get_user(db=i,user_id=2)
        print(c.email)
