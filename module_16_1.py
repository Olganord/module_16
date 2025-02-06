from fastapi import FastAPI
# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута

@app.get("/")
async def  get_main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admin_page():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_number():
    return {"message": "Вы вошли как пользователь № 123"}

@app.get("/user")
async def get_user_info():
    return {"message": "Информация о пользователе. Имя: 'Ilya', возраст: 24"}

# uvicorn module_16_1:app --reload
