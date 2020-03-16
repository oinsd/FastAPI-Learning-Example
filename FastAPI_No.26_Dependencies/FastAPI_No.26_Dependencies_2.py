# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI

app = FastAPI()
# 类作为依赖项

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# common = CommonQueryParams(),可调用，所以可以做为‘依赖’，FastAPI就会分析定义了参数
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        # __init__用于创建类实例的方法，且这些参数是FastAPI将用来“解决”依赖关系的参数
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)): # 声明依赖项。FastAPI来了解依赖项的内容
                            # CommonQueryParams FastAPI没有任何特殊含义。不会将其用于数据转换，验证等
# async def read_items(commons=Depends(CommonQueryParams)): √√√√√
# async def read_items(commons: CommonQueryParams = Depends()): √√√√√ 在相关性是明确的类的情况下
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    # items = fake_items_db[commons.skip: commons.skip + commons.limit]
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


