from fastapi import Depends, FastAPI, Header, HTTPException

from routers import users,items
# from .routers import items, users

app = FastAPI()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token": # 假超密令牌
        raise HTTPException(status_code=400, detail="X-Token header invalid") # X令牌头无效


app.include_router(users.router)
app.include_router(items.router,
    # 前缀
    prefix="/items",
    tags=["items"],
    # 依赖关系
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)