# -*- coding: UTF-8 -*-
from datetime import datetime, time, timedelta
from uuid import UUID
from uuid import uuid1
from pydantic import BaseModel
from fastapi import Body, FastAPI

app = FastAPI()

class Item(BaseModel):
    start_datetime: datetime
    end_datetime: datetime
    repeat_at: time 
    process_after: timedelta 
    start_process: str 
    duration: str 

# 额外数据类型
# https://fastapi.tiangolo.com/tutorial/extra-data-types/
@app.put("/items/{item_id}")
async def read_items(item_id: UUID, item: Item):
    item.start_process = item.start_datetime + item.process_after
    item.duration = item.end_datetime - item.start_process
    return {"item_id": item_id, 'item':item }
    

if __name__ == '__main__':
    import uvicorn
    print('uuid:', uuid1())
    uvicorn.run(app, host="127.0.0.1", port=8000)

