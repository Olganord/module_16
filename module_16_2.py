from fastapi import FastAPI
from typing import Annotated
from fastapi import Path

app = FastAPI()

@app.get('/')
async def main_page():
    return 'Главная страница'

@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'

# @app.get('/user/{user_id}')
# async def user(user_id: int):
#     return f'Вы вошли как пользователь №{user_id}'

@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[int, Path(ge=1, le=100,title="User ID", description="Enter User ID", example=1)]):
    return {"user_id": user_id}

@app.get('/user/{username}/{age}')
async def info_user(username: Annotated[str, Path(ge=5, le=20,  title='Enter username' , description="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120,  title='Enter age'  , description="Enter age", example=24)]):
        return f'Информация о пользователе. Имя: {username}, возраст: {age}'
# uvicorn module_16_2:app --reload
#