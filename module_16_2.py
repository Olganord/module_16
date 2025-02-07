from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута

@app.get("/")
async def  get_main_page():
    # return {"message": "Главная страница"}
    pass
# @app.get("/user/admin")
# async def get_admin_page():
#     return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_by_id(user_id: Annotated[int, Path(ge=1, le=100, title="ID of the user", description="Enter User ID",
                                                 example=1)]):
    return {"user_id": user_id}

@app.get('/user/{username}/{age}')
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20,  title='Username' ,
                                                      description="Enter username",
                                                  example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120,  title='Age'  , description="Enter age", example=24)]):
        return {"username": username, "age": age}

# @app.get("/user")
# async def get_user_info():
#     return {"message": "Информация о пользователе. Имя: 'Ilya', возраст: 24"}

# uvicorn module_16_2:app --reload
