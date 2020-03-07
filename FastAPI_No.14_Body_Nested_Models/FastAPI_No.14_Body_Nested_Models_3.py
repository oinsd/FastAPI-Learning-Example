# -*- coding: UTF-8 -*-
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl    # 该字符串将被检查为有效的URL，并在JSON Schema / OpenAPI中进行记录。
                    # 特殊类型和验证 https://pydantic-docs.helpmanual.io/usage/types/
    name: str

# 纯列表体
@app.post("/images/multiple/")
async def create_multiple_images(*, images: List[Image]):
    return images

# 任意dicts (无需事先知道有效的字段/属性名称是什么)(如果您想接收未知的密钥，这将很有用。)
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]): 
    return weights



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

