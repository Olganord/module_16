from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page():
    return 'Главная страница'

@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def user(user_id: int):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user')
async def info_user(user_name: str, user_age: int):
    return f'Информация о пользователе. Имя: {user_name}, возраст: {user_age}'

