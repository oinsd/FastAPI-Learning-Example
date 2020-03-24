from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI()


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str = None): # , xxx:str = None
    if q:
        message = f"found query: {q}\n"
        # print(xxx)
        print('q', id(q)); print(q)
        print(type(background_tasks)); print('first', background_tasks)
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, xxx: str = Depends(get_query)
):
    print('xxx', id(xxx));print(xxx)
    print(type(background_tasks)); print(background_tasks)
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)