# -*- coding: UTF-8 -*-
from fastapi import FastAPI, Header
from typing import List
app = FastAPI()


@app.get("/items/")
async def read_items(*, user_agent: str = Header(None), users_agent: str = Header(None)):
    return  {"User-Agent": user_agent},{"AAAAA": user_agent},{'ABCD': users_agent}
            
@app.get("/items2/")
async def read_items2(x_token: List[str] = Header(None)):
    return {"X-Token values": x_token}
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)