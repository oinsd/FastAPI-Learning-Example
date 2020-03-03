# -*- coding: UTF-8 -*-
from starlette.requests import Request
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/user/")
async def form_text(request: Request, username: str = Form(...), password: str = Form(...)):
    
    print('username',username)
    print('password',password)
    
    # return {'text_1':text_1 , 'text_2': text_2}
    return templates.TemplateResponse('index.html', {'request': request, 'username': username, 'password': password})


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('post.html', {'request': request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
