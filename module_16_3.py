from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Данные пользователей хранятся в словаре
users = {"1": "Имя: Example, возраст: 18"}


class User(BaseModel):
    # Модель данных для обработки информации о пользователе
    username: Annotated[str, Path(ge=5, le=20, description="Enter username", example="NewUser")]
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="22")]


@app.get("/user")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20,  description="Enter username", example="UrbanUser", )]
                      , age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = f"Имя: {username}, возраст: {age}"
    return f"User {current_user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(gt=0, description="Enter user_id")], username: Annotated[
    str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")]
                      , age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="28")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(gt=0, description="Enter user_id")]) -> str:
    try:
        del users[str(user_id)]
        return f"User {user_id} has been deleted."
    except KeyError:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} does not exist.")
# uvicorn module_16_3:app --reload
