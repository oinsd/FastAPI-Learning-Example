from sqlalchemy.orm import Session # 会话

import models, schemas # 模式

# 通过id查询用户信息
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
                                # 过滤器
# 通过email查询用户信息
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# 通过id范围查询用户信息
def get_users(db: Session, skip: int = 0, limit: int = 100):
                         # 初值           末值
    return db.query(models.User).offset(skip).limit(limit).all()

# 新建用户
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 获取用户拥有的项目
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

# 新建用户拥有的项目
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
